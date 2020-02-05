# pcl-gradient-comparatives
Stimuli and setup for comparative experiment through MIT's Psycholinguistics Lab to test users on comparative adjectives.

This experiment is currently hosted at http://eecoppock.info/lschex/gradient-comp-exp/welcome.cgi. The user is presented with several images, but is told that the one highlighted in red is special in some way (bigger, long, dark, etc.). The user must then use the slider to decide how well the instructions actually describe the scene. This is intended to capture user uncertainty about comparative objects when given more than two objects (the "bigger" of four objects is a more unusual description than the "bigger" of two).

In order for this experiment to actually work, the following must be populated:
1. "items.csv" must include a line for each experiment. Note that the current iteration includes repeat lines, but not repeat item numbers. It is suggested that you use 18 different items, as there are 18 different situations to test in (comparative/non-comparative X baseline/progressive/gap X 2/3/4 items). Each item is reported as the following: item number, figure, comparative adjective (ie: bigger), non-comparative adjective (ie: big).
2. Images must be populated in a folder called "images". There should be 5 images prepared for each potential scene, and they should exist as a gradient of 1-5 (ie: for a scene about the "largest" box, box_5.img should be the largest and box_1 should be the smallest).


The results.txt file for each user will have a line for each scene the user responded to. It is populated with the following information: usernum itemnum [non/comp]:[baseline/gap/prog]:numitems [non/comp]  [baseline/gap/prog] numitems  figure  USER_RESPONSE date  phrase
Example: "236	target-9	non:gap:2	non	gap	2	square	50	Fri Jan 24 17:51:34 2020	 the dark
 square".
