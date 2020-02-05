#!/usr/bin/perl

use CGI qw(:standard); print "Content-type: text/html\n\n";

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
print "<h1>Welcome!</h1>\n";

print "<p>Thanks for participating in our study! Your participation will help us learn about how listeners understand what descriptions are referring to.</p>\n";

print "<p>As you navigate through the study, you will go through a series of [X] scenes. Each scene contains two to four pictures. The instructions at the top will describe the picture highlighted in red. Use the slider to describe how accurately the instructions describe the picture.</p>\n";

print "<p>The full session should take about 10 minutes. A progress indicator will tell you how far along you are.</p>\n";

print "<p>Note that some questions are included to make sure that you are really paying attention and taking the task seriously, and approval is contingent on answering these correctly.</p>\n";

print "<p>There are no other foreseeable risks or discomforts associated with participating in this project.</p>\n";

print "<p>The information that you share on this page will be stored
  exclusively in a private location on a password-protected server
  maintained by Boston University, and it will not be shared with
  anyone outside the research team.</p>";

print "<p>Your participation in this research is voluntary. You may decline to answer any or all of the following questions. You may decline further participation at any time without adverse consequences. No personal or identifying information about you will be shared with anyone else.</p>";

print "<p>This survey is being carried out through the Linguistic
Semantics Lab [LiSLab], an international collaboration between Boston
University and the University of Gothenburg. If you have any questions or concerns, please contact Elizabeth Coppock at ecoppock" . '@' . "bu.edu.</p>";


print "<p>By clicking \"I agree\" below you are indicating that you are at least 18 years old, have read and understood the information above and agree to participate in this research study.</p>";

print "<form method=post action=startsurvey.cgi><p>";

print "<p><input type=\"checkbox\" name=\"consent\"> I agree!</p>";

print "Prolific ID: <input type=\"text\" name=\"workerID\" required /><br><br>";

print "Are you using a laptop or desktop computer? (Otherwise the survey won't work properly.)<br>";
print "<input type=radio name=computer value=yes> Yes<br>";
print "<input type=radio name=computer value=no> No<br><br>\n";
# print "What do you hear when you click on the audio below?<br>";
# print "<audio controls id=\"audio-button\">
#   <source src=\"audio/practice-1.mp3\" type=\"audio/mpeg\" alt=\"Audio test\">
# Your browser does not support the audio element.
# </audio><br>\n";

# print "Enter what you heard here: <br> <input type=text size=70 name=audio value=\"\"><br> (Make sure your sound settings are adjusted so you can hear it clearly.) <br><br>";
print "Are you in a quiet, distraction-free place? (Recommended.)<br>";
print "<input type=radio name=room value=yes> Yes<br>";
print "<input type=radio name=room value=no> No<br><br>\n";
# print "Are you wearing headphones? (Recommended especially if you are not in a quiet place.)<br>";
# print "<input type=radio name=headphones value=yes> Yes<br> ";
# print "<input type=radio name=headphones value=no> No<br><br>\n";
print "Are you in full-screen mode on your browser? (If not, please enter it now!)<br>";
print "<input type=radio name=fullscreen value=yes> Yes<br> ";
print "<input type=radio name=fullscreen value=no> No<br><br>\n";
print "<input type=submit value=\"Continue\">";
print "</form>";

print "</div>";
print "</div>";
print "</div>";

print "<div id=\"preload\">";
print "<img src=\"images/big_bag.png\" width=1 height=1 alt=\"big_bag.png\" />
<img src=\"images/big_basket.png\" width=1 height=1 alt=\"big_basket.png\" />
<img src=\"images/big_bathtub.png\" width=1 height=1 alt=\"big_bathtub.png\" />
<img src=\"images/big_boat.png\" width=1 height=1 alt=\"big_boat.png\" />
<img src=\"images/big_box.png\" width=1 height=1 alt=\"big_box.png\" />
<img src=\"images/big_bucket.png\" width=1 height=1 alt=\"big_bucket.png\" />
<img src=\"images/big_cake.png\" width=1 height=1 alt=\"big_cake.png\" />
<img src=\"images/big_can.png\" width=1 height=1 alt=\"big_can.png\" />
<img src=\"images/big_car.png\" width=1 height=1 alt=\"big_car.png\" />
<img src=\"images/big_carrot.png\" width=1 height=1 alt=\"big_carrot.png\" />
<img src=\"images/big_chair.png\" width=1 height=1 alt=\"big_chair.png\" />
<img src=\"images/big_cheese.png\" width=1 height=1 alt=\"big_cheese.png\" />
<img src=\"images/big_cherries.png\" width=1 height=1 alt=\"big_cherries.png\" />
<img src=\"images/big_cookie.png\" width=1 height=1 alt=\"big_cookie.png\" />
<img src=\"images/big_cup.png\" width=1 height=1 alt=\"big_cup.png\" />
<img src=\"images/big_dog.png\" width=1 height=1 alt=\"big_dog.png\" />
<img src=\"images/big_doll.png\" width=1 height=1 alt=\"big_doll.png\" />
<img src=\"images/big_duck.png\" width=1 height=1 alt=\"big_duck.png\" />
<img src=\"images/big_fan.png\" width=1 height=1 alt=\"big_fan.png\" />
<img src=\"images/big_fish.png\" width=1 height=1 alt=\"big_fish.png\" />
<img src=\"images/big_flower.png\" width=1 height=1 alt=\"big_flower.png\" />
<img src=\"images/big_glasses.png\" width=1 height=1 alt=\"big_glasses.png\" />
<img src=\"images/big_glue.png\" width=1 height=1 alt=\"big_glue.png\" />
<img src=\"images/big_grapes.png\" width=1 height=1 alt=\"big_grapes.png\" />
<img src=\"images/big_ladder.png\" width=1 height=1 alt=\"big_ladder.png\" />
<img src=\"images/big_lamp.png\" width=1 height=1 alt=\"big_lamp.png\" />
<img src=\"images/big_lizard.png\" width=1 height=1 alt=\"big_lizard.png\" />
<img src=\"images/big_paintbrush.png\" width=1 height=1 alt=\"big_paintbrush.png\" />
<img src=\"images/big_pen.png\" width=1 height=1 alt=\"big_pen.png\" />
<img src=\"images/big_pillow.png\" width=1 height=1 alt=\"big_pillow.png\" />
<img src=\"images/big_sandwich.png\" width=1 height=1 alt=\"big_sandwich.png\" />
<img src=\"images/big_scarf.png\" width=1 height=1 alt=\"big_scarf.png\" />
<img src=\"images/big_sock.png\" width=1 height=1 alt=\"big_sock.png\" />
<img src=\"images/big_tower.png\" width=1 height=1 alt=\"big_tower.png\" />
<img src=\"images/big_tree.png\" width=1 height=1 alt=\"big_tree.png\" />
<img src=\"images/big_truck.png\" width=1 height=1 alt=\"big_truck.png\" />
<img src=\"images/bird-big_bathtub.png\" width=1 height=1 alt=\"bird-big_bathtub.png\" />
<img src=\"images/bird-big_boat.png\" width=1 height=1 alt=\"bird-big_boat.png\" />
<img src=\"images/bird-big_bucket.png\" width=1 height=1 alt=\"bird-big_bucket.png\" />
<img src=\"images/bird-big_can.png\" width=1 height=1 alt=\"bird-big_can.png\" />
<img src=\"images/bird-big_cup.png\" width=1 height=1 alt=\"bird-big_cup.png\" />
<img src=\"images/bird-big_tower.png\" width=1 height=1 alt=\"bird-big_tower.png\" />
<img src=\"images/bird-big_tree.png\" width=1 height=1 alt=\"bird-big_tree.png\" />
<img src=\"images/bird-big_truck.png\" width=1 height=1 alt=\"bird-big_truck.png\" />
<img src=\"images/bird-med_bathtub.png\" width=1 height=1 alt=\"bird-med_bathtub.png\" />
<img src=\"images/bird-med_bucket.png\" width=1 height=1 alt=\"bird-med_bucket.png\" />
<img src=\"images/bird-med_can.png\" width=1 height=1 alt=\"bird-med_can.png\" />
<img src=\"images/bird-med_cup.png\" width=1 height=1 alt=\"bird-med_cup.png\" />
<img src=\"images/bird-med_tree.png\" width=1 height=1 alt=\"bird-med_tree.png\" />
<img src=\"images/bird-med_truck.png\" width=1 height=1 alt=\"bird-med_truck.png\" />
<img src=\"images/bird-small_bathtub.png\" width=1 height=1 alt=\"bird-small_bathtub.png\" />
<img src=\"images/bird-small_bucket.png\" width=1 height=1 alt=\"bird-small_bucket.png\" />
<img src=\"images/bird-small_can.png\" width=1 height=1 alt=\"bird-small_can.png\" />
<img src=\"images/bird-small_cup.png\" width=1 height=1 alt=\"bird-small_cup.png\" />
<img src=\"images/bird-small_tree.png\" width=1 height=1 alt=\"bird-small_tree.png\" />
<img src=\"images/bird-small_truck.png\" width=1 height=1 alt=\"bird-small_truck.png\" />
<img src=\"images/boy-big_cake.png\" width=1 height=1 alt=\"boy-big_cake.png\" />
<img src=\"images/boy-big_carrot.png\" width=1 height=1 alt=\"boy-big_carrot.png\" />
<img src=\"images/boy-big_cookie.png\" width=1 height=1 alt=\"boy-big_cookie.png\" />
<img src=\"images/boy-big_paintbrush.png\" width=1 height=1 alt=\"boy-big_paintbrush.png\" />
<img src=\"images/boy-big_pillow.png\" width=1 height=1 alt=\"boy-big_pillow.png\" />
<img src=\"images/boy-box.png\" width=1 height=1 alt=\"boy-box.png\" />
<img src=\"images/boy-med_carrot.png\" width=1 height=1 alt=\"boy-med_carrot.png\" />
<img src=\"images/boy-med_cookie.png\" width=1 height=1 alt=\"boy-med_cookie.png\" />
<img src=\"images/boy-med_paintbrush.png\" width=1 height=1 alt=\"boy-med_paintbrush.png\" />
<img src=\"images/boy-med_pillow.png\" width=1 height=1 alt=\"boy-med_pillow.png\" />
<img src=\"images/boy-small_carrot.png\" width=1 height=1 alt=\"boy-small_carrot.png\" />
<img src=\"images/boy-small_cookie.png\" width=1 height=1 alt=\"boy-small_cookie.png\" />
<img src=\"images/boy-small_paintbrush.png\" width=1 height=1 alt=\"boy-small_paintbrush.png\" />
<img src=\"images/boy-small_pillow.png\" width=1 height=1 alt=\"boy-small_pillow.png\" />
<img src=\"images/brown_frog.png\" width=1 height=1 alt=\"brown_frog.png\" />
<img src=\"images/car-tall_trafficlight.png\" width=1 height=1 alt=\"car-tall_trafficlight.png\" />
<img src=\"images/cat-big_ladder.png\" width=1 height=1 alt=\"cat-big_ladder.png\" />
<img src=\"images/cat-big_lamp.png\" width=1 height=1 alt=\"cat-big_lamp.png\" />
<img src=\"images/cat-big_lizard.png\" width=1 height=1 alt=\"cat-big_lizard.png\" />
<img src=\"images/cat-big_tree.png\" width=1 height=1 alt=\"cat-big_tree.png\" />
<img src=\"images/cat-big_truck.png\" width=1 height=1 alt=\"cat-big_truck.png\" />
<img src=\"images/cat-cup.png\" width=1 height=1 alt=\"cat-cup.png\" />
<img src=\"images/cat-med_ladder.png\" width=1 height=1 alt=\"cat-med_ladder.png\" />
<img src=\"images/cat-med_lizard.png\" width=1 height=1 alt=\"cat-med_lizard.png\" />
<img src=\"images/cat-med_tree.png\" width=1 height=1 alt=\"cat-med_tree.png\" />
<img src=\"images/cat-med_truck.png\" width=1 height=1 alt=\"cat-med_truck.png\" />
<img src=\"images/cat-short_bottle.png\" width=1 height=1 alt=\"cat-short_bottle.png\" />
<img src=\"images/cat-small_ladder.png\" width=1 height=1 alt=\"cat-small_ladder.png\" />
<img src=\"images/cat-small_lizard.png\" width=1 height=1 alt=\"cat-small_lizard.png\" />
<img src=\"images/cat-small_tree.png\" width=1 height=1 alt=\"cat-small_tree.png\" />
<img src=\"images/cat-small_truck.png\" width=1 height=1 alt=\"cat-small_truck.png\" />
<img src=\"images/cat-tall_bottle.png\" width=1 height=1 alt=\"cat-tall_bottle.png\" />
<img src=\"images/chessboard.png\" width=1 height=1 alt=\"chessboard.png\" />
<img src=\"images/dog-big_cup.png\" width=1 height=1 alt=\"dog-big_cup.png\" />
<img src=\"images/dog-short_lamp.png\" width=1 height=1 alt=\"dog-short_lamp.png\" />
<img src=\"images/dog-small_cup.png\" width=1 height=1 alt=\"dog-small_cup.png\" />
<img src=\"images/dot-b-triangle.png\" width=1 height=1 alt=\"dot-b-triangle.png\" />
<img src=\"images/elephant-box.png\" width=1 height=1 alt=\"elephant-box.png\" />
<img src=\"images/elephant-fan.png\" width=1 height=1 alt=\"elephant-fan.png\" />
<img src=\"images/elephant-glasses.png\" width=1 height=1 alt=\"elephant-glasses.png\" />
<img src=\"images/elephant.png\" width=1 height=1 alt=\"elephant.png\" />
<img src=\"images/farmer-big_chair.png\" width=1 height=1 alt=\"farmer-big_chair.png\" />
<img src=\"images/farmer-big_cheese.png\" width=1 height=1 alt=\"farmer-big_cheese.png\" />
<img src=\"images/farmer-med_chair.png\" width=1 height=1 alt=\"farmer-med_chair.png\" />
<img src=\"images/farmer-med_cheese.png\" width=1 height=1 alt=\"farmer-med_cheese.png\" />
<img src=\"images/farmer-small_chair.png\" width=1 height=1 alt=\"farmer-small_chair.png\" />
<img src=\"images/farmer-small_cheese.png\" width=1 height=1 alt=\"farmer-small_cheese.png\" />
<img src=\"images/fork.png\" width=1 height=1 alt=\"fork.png\" />
<img src=\"images/frog-big_bag.png\" width=1 height=1 alt=\"frog-big_bag.png\" />
<img src=\"images/frog-big_basket.png\" width=1 height=1 alt=\"frog-big_basket.png\" />
<img src=\"images/frog-big_bathtub.png\" width=1 height=1 alt=\"frog-big_bathtub.png\" />
<img src=\"images/frog-big_box.png\" width=1 height=1 alt=\"frog-big_box.png\" />
<img src=\"images/frog-big_bucket.png\" width=1 height=1 alt=\"frog-big_bucket.png\" />
<img src=\"images/frog-big_glasses.png\" width=1 height=1 alt=\"frog-big_glasses.png\" />
<img src=\"images/frog-big_glue.png\" width=1 height=1 alt=\"frog-big_glue.png\" />
<img src=\"images/frog-big_grapes.png\" width=1 height=1 alt=\"frog-big_grapes.png\" />
<img src=\"images/frog-med_bag.png\" width=1 height=1 alt=\"frog-med_bag.png\" />
<img src=\"images/frog-med_bathtub.png\" width=1 height=1 alt=\"frog-med_bathtub.png\" />
<img src=\"images/frog-med_box.png\" width=1 height=1 alt=\"frog-med_box.png\" />
<img src=\"images/frog-med_bucket.png\" width=1 height=1 alt=\"frog-med_bucket.png\" />
<img src=\"images/frog-med_glue.png\" width=1 height=1 alt=\"frog-med_glue.png\" />
<img src=\"images/frog-med_grapes.png\" width=1 height=1 alt=\"frog-med_grapes.png\" />
<img src=\"images/frog-small_bag.png\" width=1 height=1 alt=\"frog-small_bag.png\" />
<img src=\"images/frog-small_bathtub.png\" width=1 height=1 alt=\"frog-small_bathtub.png\" />
<img src=\"images/frog-small_box.png\" width=1 height=1 alt=\"frog-small_box.png\" />
<img src=\"images/frog-small_bucket.png\" width=1 height=1 alt=\"frog-small_bucket.png\" />
<img src=\"images/frog-small_glue.png\" width=1 height=1 alt=\"frog-small_glue.png\" />
<img src=\"images/frog-small_grapes.png\" width=1 height=1 alt=\"frog-small_grapes.png\" />
<img src=\"images/girl-big_dog.png\" width=1 height=1 alt=\"girl-big_dog.png\" />
<img src=\"images/girl-big_doll.png\" width=1 height=1 alt=\"girl-big_doll.png\" />
<img src=\"images/girl-big_duck.png\" width=1 height=1 alt=\"girl-big_duck.png\" />
<img src=\"images/girl-big_paintbrush.png\" width=1 height=1 alt=\"girl-big_paintbrush.png\" />
<img src=\"images/girl-big_pen.png\" width=1 height=1 alt=\"girl-big_pen.png\" />
<img src=\"images/girl-big_pillow.png\" width=1 height=1 alt=\"girl-big_pillow.png\" />
<img src=\"images/girl-big_sandwich.png\" width=1 height=1 alt=\"girl-big_sandwich.png\" />
<img src=\"images/girl-big_scarf.png\" width=1 height=1 alt=\"girl-big_scarf.png\" />
<img src=\"images/girl-big_sock.png\" width=1 height=1 alt=\"girl-big_sock.png\" />
<img src=\"images/girl-grapes.png\" width=1 height=1 alt=\"girl-grapes.png\" />
<img src=\"images/girl-med_dog.png\" width=1 height=1 alt=\"girl-med_dog.png\" />
<img src=\"images/girl-med_duck.png\" width=1 height=1 alt=\"girl-med_duck.png\" />
<img src=\"images/girl-med_paintbrush.png\" width=1 height=1 alt=\"girl-med_paintbrush.png\" />
<img src=\"images/girl-med_pillow.png\" width=1 height=1 alt=\"girl-med_pillow.png\" />
<img src=\"images/girl-med_scarf.png\" width=1 height=1 alt=\"girl-med_scarf.png\" />
<img src=\"images/girl-med_sock.png\" width=1 height=1 alt=\"girl-med_sock.png\" />
<img src=\"images/girl-small_dog.png\" width=1 height=1 alt=\"girl-small_dog.png\" />
<img src=\"images/girl-small_duck.png\" width=1 height=1 alt=\"girl-small_duck.png\" />
<img src=\"images/girl-small_paintbrush.png\" width=1 height=1 alt=\"girl-small_paintbrush.png\" />
<img src=\"images/girl-small_pillow.png\" width=1 height=1 alt=\"girl-small_pillow.png\" />
<img src=\"images/girl-small_scarf.png\" width=1 height=1 alt=\"girl-small_scarf.png\" />
<img src=\"images/girl-small_sock.png\" width=1 height=1 alt=\"girl-small_sock.png\" />
<img src=\"images/girl-truck.png\" width=1 height=1 alt=\"girl-truck.png\" />
<img src=\"images/girl.png\" width=1 height=1 alt=\"girl.png\" />
<img src=\"images/gray_cat.png\" width=1 height=1 alt=\"gray_cat.png\" />
<img src=\"images/green_frog.png\" width=1 height=1 alt=\"green_frog.png\" />
<img src=\"images/horse-big_ladder.png\" width=1 height=1 alt=\"horse-big_ladder.png\" />
<img src=\"images/horse-big_lizard.png\" width=1 height=1 alt=\"horse-big_lizard.png\" />
<img src=\"images/horse-med_ladder.png\" width=1 height=1 alt=\"horse-med_ladder.png\" />
<img src=\"images/horse-med_lizard.png\" width=1 height=1 alt=\"horse-med_lizard.png\" />
<img src=\"images/horse-small_ladder.png\" width=1 height=1 alt=\"horse-small_ladder.png\" />
<img src=\"images/horse-small_lizard.png\" width=1 height=1 alt=\"horse-small_lizard.png\" />
<img src=\"images/horse.png\" width=1 height=1 alt=\"horse.png\" />
<img src=\"images/lady-big_chair.png\" width=1 height=1 alt=\"lady-big_chair.png\" />
<img src=\"images/lady-big_cheese.png\" width=1 height=1 alt=\"lady-big_cheese.png\" />
<img src=\"images/lady-big_cherries.png\" width=1 height=1 alt=\"lady-big_cherries.png\" />
<img src=\"images/lady-big_fan.png\" width=1 height=1 alt=\"lady-big_fan.png\" />
<img src=\"images/lady-big_fish.png\" width=1 height=1 alt=\"lady-big_fish.png\" />
<img src=\"images/lady-med_chair.png\" width=1 height=1 alt=\"lady-med_chair.png\" />
<img src=\"images/lady-med_cheese.png\" width=1 height=1 alt=\"lady-med_cheese.png\" />
<img src=\"images/lady-med_fan.png\" width=1 height=1 alt=\"lady-med_fan.png\" />
<img src=\"images/lady-med_fish.png\" width=1 height=1 alt=\"lady-med_fish.png\" />
<img src=\"images/lady-small_chair.png\" width=1 height=1 alt=\"lady-small_chair.png\" />
<img src=\"images/lady-small_cheese.png\" width=1 height=1 alt=\"lady-small_cheese.png\" />
<img src=\"images/lady-small_fan.png\" width=1 height=1 alt=\"lady-small_fan.png\" />
<img src=\"images/lady-small_fish.png\" width=1 height=1 alt=\"lady-small_fish.png\" />
<img src=\"images/long_pencil-notepad.png\" width=1 height=1 alt=\"long_pencil-notepad.png\" />
<img src=\"images/man-big_dog.png\" width=1 height=1 alt=\"man-big_dog.png\" />
<img src=\"images/man-big_doll.png\" width=1 height=1 alt=\"man-big_doll.png\" />
<img src=\"images/man-big_duck.png\" width=1 height=1 alt=\"man-big_duck.png\" />
<img src=\"images/man-big_fan.png\" width=1 height=1 alt=\"man-big_fan.png\" />
<img src=\"images/man-big_fish.png\" width=1 height=1 alt=\"man-big_fish.png\" />
<img src=\"images/man-big_flower.png\" width=1 height=1 alt=\"man-big_flower.png\" />
<img src=\"images/man-big_scarf.png\" width=1 height=1 alt=\"man-big_scarf.png\" />
<img src=\"images/man-big_sock.png\" width=1 height=1 alt=\"man-big_sock.png\" />
<img src=\"images/man-big_truck.png\" width=1 height=1 alt=\"man-big_truck.png\" />
<img src=\"images/man-med_dog.png\" width=1 height=1 alt=\"man-med_dog.png\" />
<img src=\"images/man-med_duck.png\" width=1 height=1 alt=\"man-med_duck.png\" />
<img src=\"images/man-med_fan.png\" width=1 height=1 alt=\"man-med_fan.png\" />
<img src=\"images/man-med_fish.png\" width=1 height=1 alt=\"man-med_fish.png\" />
<img src=\"images/man-med_scarf.png\" width=1 height=1 alt=\"man-med_scarf.png\" />
<img src=\"images/man-med_sock.png\" width=1 height=1 alt=\"man-med_sock.png\" />
<img src=\"images/man-small_dog.png\" width=1 height=1 alt=\"man-small_dog.png\" />
<img src=\"images/man-small_duck.png\" width=1 height=1 alt=\"man-small_duck.png\" />
<img src=\"images/man-small_fan.png\" width=1 height=1 alt=\"man-small_fan.png\" />
<img src=\"images/man-small_fish.png\" width=1 height=1 alt=\"man-small_fish.png\" />
<img src=\"images/man-small_scarf.png\" width=1 height=1 alt=\"man-small_scarf.png\" />
<img src=\"images/man-small_sock.png\" width=1 height=1 alt=\"man-small_sock.png\" />
<img src=\"images/man-small_truck.png\" width=1 height=1 alt=\"man-small_truck.png\" />
<img src=\"images/man-vacuum.png\" width=1 height=1 alt=\"man-vacuum.png\" />
<img src=\"images/man-vase.png\" width=1 height=1 alt=\"man-vase.png\" />
<img src=\"images/med_bag.png\" width=1 height=1 alt=\"med_bag.png\" />
<img src=\"images/med_bathtub.png\" width=1 height=1 alt=\"med_bathtub.png\" />
<img src=\"images/med_box.png\" width=1 height=1 alt=\"med_box.png\" />
<img src=\"images/med_bucket.png\" width=1 height=1 alt=\"med_bucket.png\" />
<img src=\"images/med_can.png\" width=1 height=1 alt=\"med_can.png\" />
<img src=\"images/med_carrot.png\" width=1 height=1 alt=\"med_carrot.png\" />
<img src=\"images/med_chair.png\" width=1 height=1 alt=\"med_chair.png\" />
<img src=\"images/med_cheese.png\" width=1 height=1 alt=\"med_cheese.png\" />
<img src=\"images/med_cookie.png\" width=1 height=1 alt=\"med_cookie.png\" />
<img src=\"images/med_cup.png\" width=1 height=1 alt=\"med_cup.png\" />
<img src=\"images/med_dog.png\" width=1 height=1 alt=\"med_dog.png\" />
<img src=\"images/med_duck.png\" width=1 height=1 alt=\"med_duck.png\" />
<img src=\"images/med_fan.png\" width=1 height=1 alt=\"med_fan.png\" />
<img src=\"images/med_fish.png\" width=1 height=1 alt=\"med_fish.png\" />
<img src=\"images/med_glue.png\" width=1 height=1 alt=\"med_glue.png\" />
<img src=\"images/med_grapes.png\" width=1 height=1 alt=\"med_grapes.png\" />
<img src=\"images/med_ladder.png\" width=1 height=1 alt=\"med_ladder.png\" />
<img src=\"images/med_lizard.png\" width=1 height=1 alt=\"med_lizard.png\" />
<img src=\"images/med_paintbrush.png\" width=1 height=1 alt=\"med_paintbrush.png\" />
<img src=\"images/med_pillow.png\" width=1 height=1 alt=\"med_pillow.png\" />
<img src=\"images/med_scarf.png\" width=1 height=1 alt=\"med_scarf.png\" />
<img src=\"images/med_sock.png\" width=1 height=1 alt=\"med_sock.png\" />
<img src=\"images/med_tree.png\" width=1 height=1 alt=\"med_tree.png\" />
<img src=\"images/med_truck.png\" width=1 height=1 alt=\"med_truck.png\" />
<img src=\"images/monkey-big_glue.png\" width=1 height=1 alt=\"monkey-big_glue.png\" />
<img src=\"images/monkey-big_grapes.png\" width=1 height=1 alt=\"monkey-big_grapes.png\" />
<img src=\"images/monkey-med_glue.png\" width=1 height=1 alt=\"monkey-med_glue.png\" />
<img src=\"images/monkey-med_grapes.png\" width=1 height=1 alt=\"monkey-med_grapes.png\" />
<img src=\"images/monkey-small_glue.png\" width=1 height=1 alt=\"monkey-small_glue.png\" />
<img src=\"images/monkey-small_grapes.png\" width=1 height=1 alt=\"monkey-small_grapes.png\" />
<img src=\"images/pl-b-circle.png\" width=1 height=1 alt=\"pl-b-circle.png\" />
<img src=\"images/pl-bl-diamond.png\" width=1 height=1 alt=\"pl-bl-diamond.png\" />
<img src=\"images/pl-g-circle.png\" width=1 height=1 alt=\"pl-g-circle.png\" />
<img src=\"images/pl-r-circle.png\" width=1 height=1 alt=\"pl-r-circle.png\" />
<img src=\"images/pl-r-square.png\" width=1 height=1 alt=\"pl-r-square.png\" />
<img src=\"images/pl-y-square.png\" width=1 height=1 alt=\"pl-y-square.png\" />
<img src=\"images/policewoman-big_carrot.png\" width=1 height=1 alt=\"policewoman-big_carrot.png\" />
<img src=\"images/policewoman-big_cookie.png\" width=1 height=1 alt=\"policewoman-big_cookie.png\" />
<img src=\"images/policewoman-med_carrot.png\" width=1 height=1 alt=\"policewoman-med_carrot.png\" />
<img src=\"images/policewoman-med_cookie.png\" width=1 height=1 alt=\"policewoman-med_cookie.png\" />
<img src=\"images/policewoman-small_carrot.png\" width=1 height=1 alt=\"policewoman-small_carrot.png\" />
<img src=\"images/policewoman-small_cookie.png\" width=1 height=1 alt=\"policewoman-small_cookie.png\" />
<img src=\"images/rabbit-big_bag.png\" width=1 height=1 alt=\"rabbit-big_bag.png\" />
<img src=\"images/rabbit-big_box.png\" width=1 height=1 alt=\"rabbit-big_box.png\" />
<img src=\"images/rabbit-big_can.png\" width=1 height=1 alt=\"rabbit-big_can.png\" />
<img src=\"images/rabbit-big_car.png\" width=1 height=1 alt=\"rabbit-big_car.png\" />
<img src=\"images/rabbit-big_cup.png\" width=1 height=1 alt=\"rabbit-big_cup.png\" />
<img src=\"images/rabbit-med_bag.png\" width=1 height=1 alt=\"rabbit-med_bag.png\" />
<img src=\"images/rabbit-med_box.png\" width=1 height=1 alt=\"rabbit-med_box.png\" />
<img src=\"images/rabbit-med_can.png\" width=1 height=1 alt=\"rabbit-med_can.png\" />
<img src=\"images/rabbit-med_cup.png\" width=1 height=1 alt=\"rabbit-med_cup.png\" />
<img src=\"images/rabbit-small_bag.png\" width=1 height=1 alt=\"rabbit-small_bag.png\" />
<img src=\"images/rabbit-small_box.png\" width=1 height=1 alt=\"rabbit-small_box.png\" />
<img src=\"images/rabbit-small_can.png\" width=1 height=1 alt=\"rabbit-small_can.png\" />
<img src=\"images/rabbit-small_cup.png\" width=1 height=1 alt=\"rabbit-small_cup.png\" />
<img src=\"images/rabbit.png\" width=1 height=1 alt=\"rabbit.png\" />
<img src=\"images/red_fish.png\" width=1 height=1 alt=\"red_fish.png\" />
<img src=\"images/short_bottle.png\" width=1 height=1 alt=\"short_bottle.png\" />
<img src=\"images/short_boy.png\" width=1 height=1 alt=\"short_boy.png\" />
<img src=\"images/short_building-antenna.png\" width=1 height=1 alt=\"short_building-antenna.png\" />
<img src=\"images/short_farmer-horse.png\" width=1 height=1 alt=\"short_farmer-horse.png\" />
<img src=\"images/short_flower.png\" width=1 height=1 alt=\"short_flower.png\" />
<img src=\"images/short_glass-plate.png\" width=1 height=1 alt=\"short_glass-plate.png\" />
<img src=\"images/short_man.png\" width=1 height=1 alt=\"short_man.png\" />
<img src=\"images/short_pencil-notepad.png\" width=1 height=1 alt=\"short_pencil-notepad.png\" />
<img src=\"images/short_pitcher-glass.png\" width=1 height=1 alt=\"short_pitcher-glass.png\" />
<img src=\"images/short_tower-flag.png\" width=1 height=1 alt=\"short_tower-flag.png\" />
<img src=\"images/short_trafficlight.png\" width=1 height=1 alt=\"short_trafficlight.png\" />
<img src=\"images/short_woman.png\" width=1 height=1 alt=\"short_woman.png\" />
<img src=\"images/small_bag.png\" width=1 height=1 alt=\"small_bag.png\" />
<img src=\"images/small_bathtub.png\" width=1 height=1 alt=\"small_bathtub.png\" />
<img src=\"images/small_box.png\" width=1 height=1 alt=\"small_box.png\" />
<img src=\"images/small_bucket.png\" width=1 height=1 alt=\"small_bucket.png\" />
<img src=\"images/small_can.png\" width=1 height=1 alt=\"small_can.png\" />
<img src=\"images/small_chair.png\" width=1 height=1 alt=\"small_chair.png\" />
<img src=\"images/small_cheese.png\" width=1 height=1 alt=\"small_cheese.png\" />
<img src=\"images/small_cookie.png\" width=1 height=1 alt=\"small_cookie.png\" />
<img src=\"images/small_cup.png\" width=1 height=1 alt=\"small_cup.png\" />
<img src=\"images/small_dog.png\" width=1 height=1 alt=\"small_dog.png\" />
<img src=\"images/small_duck.png\" width=1 height=1 alt=\"small_duck.png\" />
<img src=\"images/small_fan.png\" width=1 height=1 alt=\"small_fan.png\" />
<img src=\"images/small_fish.png\" width=1 height=1 alt=\"small_fish.png\" />
<img src=\"images/small_glue.png\" width=1 height=1 alt=\"small_glue.png\" />
<img src=\"images/small_grapes.png\" width=1 height=1 alt=\"small_grapes.png\" />
<img src=\"images/small_ladder.png\" width=1 height=1 alt=\"small_ladder.png\" />
<img src=\"images/small_lizard.png\" width=1 height=1 alt=\"small_lizard.png\" />
<img src=\"images/small_paintbrush.png\" width=1 height=1 alt=\"small_paintbrush.png\" />
<img src=\"images/small_pillow.png\" width=1 height=1 alt=\"small_pillow.png\" />
<img src=\"images/small_scarf.png\" width=1 height=1 alt=\"small_scarf.png\" />
<img src=\"images/small_sock.png\" width=1 height=1 alt=\"small_sock.png\" />
<img src=\"images/small_tree.png\" width=1 height=1 alt=\"small_tree.png\" />
<img src=\"images/small_truck.png\" width=1 height=1 alt=\"small_truck.png\" />
<img src=\"images/stripe-b-square.png\" width=1 height=1 alt=\"stripe-b-square.png\" />
<img src=\"images/stripe-g-square.png\" width=1 height=1 alt=\"stripe-g-square.png\" />
<img src=\"images/stripe-y-triangle.png\" width=1 height=1 alt=\"stripe-y-triangle.png\" />
<img src=\"images/tall_bottle.png\" width=1 height=1 alt=\"tall_bottle.png\" />
<img src=\"images/tall_boy-dog.png\" width=1 height=1 alt=\"tall_boy-dog.png\" />
<img src=\"images/tall_building-antenna.png\" width=1 height=1 alt=\"tall_building-antenna.png\" />
<img src=\"images/tall_farmer-horse.png\" width=1 height=1 alt=\"tall_farmer-horse.png\" />
<img src=\"images/tall_glass-plate.png\" width=1 height=1 alt=\"tall_glass-plate.png\" />
<img src=\"images/tall_man.png\" width=1 height=1 alt=\"tall_man.png\" />
<img src=\"images/tall_pitcher.png\" width=1 height=1 alt=\"tall_pitcher.png\" />
<img src=\"images/tall_policewoman-man.png\" width=1 height=1 alt=\"tall_policewoman-man.png\" />
<img src=\"images/tall_policewoman.png\" width=1 height=1 alt=\"tall_policewoman.png\" />
<img src=\"images/tall_tower-flag.png\" width=1 height=1 alt=\"tall_tower-flag.png\" />
<img src=\"images/tall_woman.png\" width=1 height=1 alt=\"tall_woman.png\" />
<img src=\"images/violin.png\" width=1 height=1 alt=\"violin.png\" />
<img src=\"images/yellow_bird.png\" width=1 height=1 alt=\"yellow_bird.png\" />
";
print "</div>";


print "</body></html>";
