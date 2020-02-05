#!/usr/bin/perl

use CGI qw(:standard); print "Content-type: text/html\n\n";

use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser', 'croak';

my ($query,$inputdata,@params,$num,$newnum,$itemID,%item,@randitems,$seed,@stims,@lines,@targets,@randtargets,$writedir);


$writedir = "."; #for eecoppock.info
#$writedir = "/shared/hc/pc/data";  #for semlab.bu.edu

$query=CGI->new;

print start_html(-title=>'Survey',
                 -style => { -src => '/styles/survey.css',
                             -type => 'text/css',
                             -media => 'screen' },
                 );
print "<div id=\"shade\">";
print "<p>&nbsp;</p>";
print "<p>&nbsp;</p>";
print "<div id=\"content\">";
print "<div id=\"pub\">";

@params = $query->param;


#read old usernum
open (USERNUMFILE, "usernum.txt");
while (<USERNUMFILE>) {
    chomp;
    if (/([0-9]+)/) {
	$num = $1;
      } else {
	$num = 0;
      }
}
$newnum = $num + 1;
close (USERNUMFILE);

#update it
open (USERNUMFILE, ">usernum.txt");
print USERNUMFILE $newnum;
close (USERNUMFILE);

#print user data

open (USERDATAFILE, ">$writedir/userdata/userdata-$num.txt") or print "WARNING: Cannot open userdata file";

foreach my $paramKey (@params) {
    $inputdata = $query->param($paramKey);
    print USERDATAFILE "$num\t$paramKey\t$inputdata\n";
  }

foreach my $key ("REMOTE_ADDR","REMOTE_PORT","UNIQUE_ID","HTTP_USER_AGENT") {
   print USERDATAFILE "$num\t$key\t$ENV{$key}\n";
}

close (USERDATAFILE);



print "<p>&nbsp;</p>";

print "<h1>Welcome!</h1>";

print "<p>Thanks for participating!</p>
<p>Let's get started. As a reminder:</p>";

print "<p>You will see a series of scenes. Each scene contains two to four images. The instructions at the top will describe the image highlighted in red. Use the slider to describe how accurately the instructions describe the image in the scene.</p>";

print "<p><b>Note</b>: There is sometimes a tendency for the server to drop the connection. If this happens, just <i>press the 'Back' button on your browser to go to the previous question</i>, and try again. It should work. Apologies for this inconvenience if it happens.</p>";

# print "<form method=post action=\"practice-trial.cgi\">
# <input type=hidden name=usernum value=$num>
# <input type=hidden name=qnum value=0>
# <input type=submit value=\"Begin practice trials\">
# </form>";
print "<form method=post action=\"display-question.cgi\">
<input type=hidden name=usernum value=$num>
<input type=hidden name=qnum value=0>
<input type=submit value=\"Let's begin!\"  id=begin>
</form> </p>";

close (USERDATAFILE);

open (STIMFILE,"items.csv") or print "Can't find items.csv";

@lines = <STIMFILE>;


foreach my $line (@lines) {
    chomp;
    my ($itemnum,@rest) = split(/,/,$line);
    if ($itemnum =~ m/[0-9]/) {
      push(@targets,"target-$itemnum");
    }
  }

close (STIMFILE);


@randtargets = randarray(@targets);

@randitems = @randtargets;

#@randitems = randarray(@stims);

open (ORDERFILE,">>order.txt");

print ORDERFILE "$num @randitems\n";

close(ORDERFILE);


print "</div>";
print "</div>";
print "</div>";

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
