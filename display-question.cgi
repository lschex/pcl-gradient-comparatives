#!/usr/bin/perl

use CGI qw(:standard); print "Content-type: text/html\n\n";
use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser', 'croak';

my (
    $query,       # CGI query object
    $rand,        # random number for banners
    @params,      # array of all fields sent
    $usernum, $qnum, $itemID, $total, @order, $question, @answerIDs, $answerID, $answer, $seed, @answers, $comment,$pic,$cond,%nouns,%prep,$type,$stimnum,$phrase,@images,@nouns, $image1,$image2,$image3,$image4,$image5,$subject,%subj,$size,$time,%words,$figure,$numitems,%word,$adj,$adjtype,$cmpadj,$nonadj,$displaytype,$version,$writedir,
    );
$query=CGI->new;           # get CGI object


$writedir = ""; #for eecoppock.info
#$writedir = "/shared/hc/pc/data/";  #for semlab.bu.edu

print start_html(-title=>'Survey',
                 -style => { -src => 'survey.css',
                             -type => 'text/css',
                             -media => 'screen' },
                 );
print "<div id=\"shade\">";
print "<p>&nbsp;</p>";
print "<p>&nbsp;</p>";
print "<div id=\"content\">";
#print "<div id=\"pub\">";


#first print data from previous question

$usernum = $query->param("usernum");
$qnum = $query->param("qnum");
$cond = $query->param("cond");
$adjtype = $query->param("adjtype");
$figure = $query->param("figure");
$answer = $query->param("answer");
$time = localtime;

open (STIMFILE,"items.csv") or die "Can't find items.csv";

while (<STIMFILE>) {
    chomp;
    my ($itemnum,$figure,$cmpadj,$nonadj) = split(/,/);
    $itemnum =~ s/^[^0-9]+//; #no idea how freaky characters get on there
    $word{$itemnum}{"figure"} = $figure;
    $word{$itemnum}{"cmpadj"} = $cmpadj;
    $word{$itemnum}{"nonadj"} = $nonadj;
  }

close (STIMFILE);



open (ORDERFILE, "order.txt");

while (<ORDERFILE>) {
    chomp;
    my ($subject,@stims) = split(/ /);
    if ($subject eq $usernum) {
	@order = @stims;
    }
}
close (ORDERFILE);

$total = scalar(@order);

if ($qnum > 0) {

  open (DATAFILE, ">>$writedir data/data-$usernum.txt");
  $itemID = $order[$qnum-1];
  #($type,$stimnum) = split(/-/,$itemID);
  ($adjtype,$displaytype,$version) = split(/:/,$cond);
  print DATAFILE "$usernum\t$itemID\t$cond\t" . $adjtype . "\t" . $displaytype . "\t" . $version;
  print DATAFILE "\t$figure";
  print DATAFILE "\t" . $query->param("answer") . "\t" . $time;
  print DATAFILE "\t" . $query->param("phrase") . "\n";
  #$comment = $query->param("comments");
  #print DATAFILE "$usernum $itemID comment $comment\n";
  close (DATAFILE);

} else {
  open (USERDATAFILE, ">>$writedir userdata/userdata-$usernum.txt");
  print USERDATAFILE "$usernum\tstarttime\t$time\n";
  close (USERDATAFILE);
}



#then print next question

$qnum = $qnum+1;

if ($qnum>$total) {

 # open (USERDATAFILE, ">>userdata/userdata-$usernum.txt");
  #note below changed after run from spaces to tabs
 # print USERDATAFILE "$usernum\tendtime\t$time\n";
 # close (USERDATAFILE);

  print "<br><br><br><br><br><br><h1>All done!</h1>  <p>Thanks for participating!</p>";

  #add comments here

  print "<p>If you have any questions or comments, <br> please send an email to ecoppock" . '@' . "bu.edu.</p>";

  print "<p>Completion URL: <a href=\"https://app.prolific.co/submissions/complete?cc=1B5D01FC\">https://app.prolific.co/submissions/complete?cc=1B5D01FC</a></p>";

} else {

 print "<p id=\"progress-indicator-position\">$qnum/$total</p>";

  $itemID = $order[$qnum-1];

  ($type,$stimnum) = split(/-/,$itemID);

 $stimnum =~ s/^[^0-9]+//; #no idea how freaky characters get on there

  if ($type eq "target") {

    $figure = $word{$stimnum}{"figure"};
    $cmpadj = $word{$stimnum}{"cmpadj"};
    $nonadj = $word{$stimnum}{"nonadj"};


    $cond = get_cond($usernum,$stimnum);


#    print "cond: $cond<br>\n";

    #    print "stimnum: $stimnum<br>\n";

    if ($cond =~ m/^cmp/) {
      $adj = $cmpadj;
      $phrase = " the " . $cmpadj . " " . $figure;
      $adjtype = "cmp";
    } elsif ($cond =~ m/non/) {
      $adj = $nonadj;
      $phrase = " the " . $nonadj . " " . $figure;
      $adjtype = "non";
    } else {
      print "ERROR: Unknown cond $cond";
    }

   if ($cond  =~ m/2$/) {
    if ($cond  =~ m/baseline/) {
      $image1 = $figure . "_1" ;
      $image2 = $figure . "_5" ;
    } elsif ($cond =~ m/prog/) {
      $image1 = $figure . "_4" ;
      $image2 = $figure . "_5" ;
    } elsif ($cond =~ m/gap/) {
      $image1 = $figure . "_1" ;
      $image2 = $figure . "_2" ;
    } else {
      print "ERROR: Unknown cond $cond";
    }
    @images = ($image1, $image2);
   } elsif ($cond  =~ m/3$/) {
    if ($cond  =~ m/baseline/) {
      $image1 = $figure . "_1" ;
      $image2 = $figure . "_4" ;
      $image3 = $figure . "_5" ;
    } elsif ($cond =~ m/prog/) {
      $image1 = $figure . "_3" ;
      $image2 = $figure . "_4" ;
      $image3 = $figure . "_5" ;
    } elsif ($cond =~ m/gap/) {
      $image1 = $figure . "_1" ;
      $image2 = $figure . "_2" ;
      $image3 = $figure . "_5" ;
    } else {
      print "ERROR: Unknown cond $cond";
    }
    @images = ($image1, $image2, $image3);
   } elsif ($cond  =~ m/4$/) {
    if ($cond  =~ m/baseline/) {
      $image1 = $figure . "_1" ;
      $image2 = $figure . "_3" ;
      $image3 = $figure . "_4" ;
      $image4 = $figure . "_5" ;
    } elsif ($cond =~ m/prog/) {
      $image1 = $figure . "_2" ;
      $image2 = $figure . "_3" ;
      $image3 = $figure . "_4" ;
      $image4 = $figure . "_5" ;
    } elsif ($cond =~ m/gap/) {
      $image1 = $figure . "_1" ;
      $image2 = $figure . "_2" ;
      $image3 = $figure . "_4" ;
      $image4 = $figure . "_5" ;
    } else {
      print "ERROR: Unknown cond $cond";
    }
    @images = ($image1, $image2, $image3, $image4);
   } else {
    print "ERROR: UNKNOWN TYPE $type with itemID $itemID\n";
   }
  }

  my $i = 1;

  my @positionorder = randarray(1,2,3,4);

 foreach my $image (@images) {

   $image =~ s/[^a-z-_12345]//g;

#   print "[$image] ";

   $size = 160;

    my $position = $positionorder[$i-1];

    print "<label>\n";

#     print  "<input type=submit> <img src=\"images/$image.png\" width=$size id=\"object-position-$position\", alt=\"$image.png\"\">\n";
    if ($image eq $image1) {
      print  "<img src=\"images/$image.png\" width=$size id=\"object-position-$position\", alt= \"$image\" style=\"-webkit-filter: drop-shadow(0px 0px 15px #f00);\">\n";
    } else {
      print  "<img src=\"images/$image.png\" width=$size id=\"object-position-$position\", alt= \"$image\">\n";
    }
    print "</label>";

    print "</form>";


    $i++;
  }

 # print "<p id=audio-button>Click on the $phrase.<br>cond $cond</p>";

 # print"    <script>
 #  function play(){
 #       var audio = document.getElementById(\"audio-button\");
 #       audio.play();
 #                 }
 #   </script>";


print "<p class=\"myInstructions\">This is $phrase.</p>";
print "<p class=\"myGaugeStatement\">How acceptable is this description?</p>";
print "<p class=\"leftStatement\">Very Bad</p>";
print "<p class=\"rightStatement\">Very Good</p>";

print "<form method=post action=display-question.cgi name=form>\n";

print "<input type=hidden name=usernum value=\"$usernum\">\n";
print "<input type=hidden name=cond value=\"$cond\">\n";
print "<input type=hidden name=adjtype value=\"$adjtype\">\n";
print "<input type=hidden name=figure value=\"$figure\">\n";
print "<input type=hidden name=qnum value=\"$qnum\">\n";
print "<input type=hidden name=itemID value=\"$itemID\">\n";
print "<input type=hidden name=phrase value=\"$phrase\">\n";
print "<input type=\"range\" name=answer min=\"1\" max=\"100\" value=\"50\" class=\"slider\" id=\"myRange\">";
# print" <div class=\"dropdown\">
#   <button onclick=\"myFunction()\" class=\"dropbtn\">Dropdown</button>
#   <div id=\"myDropdown\" class=\"dropdown-content\">
#     <a href=\"#\">(Really Bad)1</a>
#     <a href=\"#\">2</a>
#     <a href=\"#\">3</a>
#     <a href=\"#\">4</a>
#     <a href=\"#\">5 (Perfect!)</a>
#   </div>
# </div>";
print "<button type=\"button\" class=\"myButton\" onclick=\"checkform();\">Next</button>";


 # older working version
#  print "<div id=\"audio-button\"><audio controls >
#   <source src=\"audio/$audiofile.mp3\" type=\"audio/mpeg\" alt=\"Click on the $phrase.\">
# Your browser does not support the audio element.
# </audio><br>Click on the $phrase.</div>\n";


}


#print "</div>";
print "</div>";
print "</div>";

 print "
 <script>
 function checkform() {
    document.form.submit();
  }
 </script>";

print "
<script>
var slider = document.getElementById(\"myRange\");
var output = document.getElementById(\"demo\");
output.innerHTML = 50; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}
</script>";

print "</body></html>";


sub randarray {
        my @array = @_;
        my @rand = undef;
        $seed = $#array + 1;
        my $randnum = int(rand($seed));
        $rand[$randnum] = shift(@array);
        while (1) {
                my $randnum = int(rand($seed));
                if ($rand[$randnum] eq undef) {
                        $rand[$randnum] = shift(@array);
                }
                last if ($#array == -1);
        }
        return @rand;
}


sub get_cond {
  my ($usernum,$itemnum) = @_;
  my @conds = ("cmp:baseline:2","cmp:prog:2","cmp:gap:2",
         "cmp:baseline:3","cmp:prog:3","cmp:gap:3",
	       "cmp:baseline:4","cmp:prog:4","cmp:gap:4",
         "non:baseline:2","non:prog:2","non:gap:2",
         "non:baseline:3","non:prog:3","non:gap:3",
       	 "non:baseline:4","non:prog:4","non:gap:4"
	      );
  my $i = ($usernum+$itemnum) % 18;
  my $cond = $conds[$i];
  return $cond;
}
