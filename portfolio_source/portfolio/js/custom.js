/// <reference path="path-to-vsdoc-file" />

function highlight(ID) {

	// This function creates an array of information.  When an item from the grid is selected, the information is displayed in
	// the "Highlight" div.

	var highlightInfo = new Array(
/* 0: Personal Blog */		"I've kept a regularly updated <a href='http://www.shaunagm.net/blog' target='_blank'>personal blog</a> since January 2010.<br /><br />My favorite posts include:<br /><a href='http://www.shaunagm.net/blog/2013/10/hacking-the-hackathon/' target='_blank'>Hacking the Hackathon</a><br /><a href='http://www.shaunagm.net/blog/2013/02/how-to-find-a-statistically-significant-other/' target='_blank'>How to Find a Statistically Significant Other</a><br /><a href='http://www.shaunagm.net/blog/2011/02/greatness-and-depression/' target='_blank'>Lincoln's Inner War</a>",
/* 1: OpenHatch Blog */		"[NOT IN USE] - include as part of 'OpenHatch' item",
/* 2: OSC */			"The Open Science Collective is a group of open science activists affiliated with the <a href='http://centerforopenscience.org/' target='_blank'>Center for Open Science</a>.  Currently I am focusing on <a href='http://osc.centerforopenscience.org/' target='_blank'>the OSC blog</a> for which I write and manage the statistics and methods section.  I also contribute to the code base that runs the blog.<br /><br />I have several small research projects I am undertaking in collaboration with members of the OSC.",
/* 3: Fiction */		"I've been writing most of my life, but I've only started trying to publish recently, so I have exactly one published piece:<br /><br /><a href='http://issue.liquid-imagination.com/article/hibernation-by-shauna-gordon-mckeon/' target='_blank'>Hibernation</a>, published 2/2013 in Liquid Imagination<br /><br />I also have a few pieces I have no plan on publishing, which I've released under a CC-BY-SA license:<br /><br />Silence - a retelling of the Little Mermaid<br />The Cry of the Crow – historical fiction set around 2380 BC, centering on Urukagina of Lagash<br /><br />You can also browse through <a href='http://www.shaunagm.net/blog/writing/' target='_blank'>blog posts tagged writing</a>.",
/* 4: Web Des & Dv */		"I have done a small amount of freelance and volunteer web development, mostly using Wordpress.  My work includes:<br /><br /><a href=''>Purple Fields</a> Wordpress theme<br /><br />Shulamis publicity site (<a href=''>screenshots</a>)<br /><br /> <a href=''>adapted Comments Vote plugin</a> for The Hathor Legacy<br /><br /> a Wordpress website for <a href='http://childrenscharter.org/'>Children's Charter</a> built during a hackathon (not their current site) <br /><br />and this portfolio page, built using the <a href='http://mixitup.io/'>MixItUp</a> plugin<br />",
/* 5: MediaLab */		"Media Lab [dates, responsibilities]",
/* 6: Laser Lab */		"In the winter of 2011, I spent four months working part time at an <a href='http://www.seas.harvard.edu/matsci/people/aziz/aziz.html'>'Energy Technology' lab</a> - that is, a laser lab!  I built a graphical user interface in Matlab so that lab members could adjust settings, operate the laser and collect data from multiple senors without having to learn to program.<br /><br />The image in the thumbnail is a space invader burned onto a sheet of metal using the GUI that I created.",
/* 7: OpenHatch */		"<a href='http://openhatch.org/' target='_blank'>OpenHatch</a> is a small non-profit dedicated to helping newcomers find their way into open source communities.  I organize <a href='http://campus.openhatch.org/' target='_blank'>Open Source Comes to Campus</a>, a series of workshops on college campuses introducing students to open source tools like issue trackers and version control and helping them make their first contributions to projects.  We've run twelve events since I joined in January 2013.  Our goal is to document our process and materials thoroughly so anyone who wants to can run our events.  You can see our progress with that (<a href='https://openhatch.org/wiki/OSCTC_logistics' target='_blank'>wiki</a>, <a href='https://github.com/openhatch/open-source-comes-to-campus' target='_blank'>github</a>).<br /><br />In addition to these campus events, I write for <a href='http://openhatch.org/blog/author/shauna/' target='_blank'>the OpenHatch blog</a>, work with open source projects to make them more accessible/welcoming, and work on improving our curriculum and outreach in various ways.",
/* 8: Parts & Crafts */		"<a href='http://partsandcrafts.org/' target='_blank'>Parts and Crafts</a> is a homeschooling center and summer camp run with an 'unschooling' philosophy.  It's frequently referred to as a hackerspace for kids.  I have been teaching at Parts and Crafts on and off since the summer of 2010 and have led a variety of activities, including: <a href='http://www.shaunagm.net/blog/2010/09/learning-in-the-time-of-cholera/' target='_blank'>roleplaying a cholera outbreak</a>, <a href='http://www.shaunagm.net/blog/2011/01/community-supported-education/' target='_blank'>making telegraphs</a>, drawing a giant board game on the floor, playing baseball and computing baseball statistics, <a href='http://www.shaunagm.net/blog/2012/07/one-time-at-hackerspace-freeschool-camp/' target='_blank'>high speed photography</a>, <a href='http://www.shaunagm.net/blog/2011/08/hunting-grounds/' target='_blank'>making and running a kids' puzzle hunt</a>, and more.",
/* 9: SIG */			"Summer Institute for the Gifted [dates, responsibilities], link to SIG materials on github",
/* 10: OpenGovBoston */		"description, link to meetup, Intro to Prog Using OpenGov (continuing with Mako), maybe Follow the Money?",
/* 11: Moral Cog Lab */		"Moral Cognition Lab [dates, responsibilities (mention how it fits categories), assoc pubs/presentations]",
/* 12: UC Davis */		"UC Davis Imaging RC [dates, responsibilities (mention how it fits categories), assoc pubs/presentations]",
/* 13: Yerkes */		"Yerkes",
/* 14: Hampshire */		"Educational details!  Reference Div III?",
/* 15: Div III */		"Div III [describe it, link to Hampshire site?, explain not digitized, associated pubs/presentations]",
/* 16: WC Weekly */		"Digitizing WCWeekly (link!)",
/* 17: Poli Internships */	"List/describe political internships?",
/* 18: One time events */	"List one time events? (see to do for structure thoughts)",
/* 19: TA CogNeuro */		"[NOT IN USE] - include under Hampshire College",
/* 20: Non-degree CW */		"[NOT IN USE] - perhaps list non-degree courses from Harvard Extension, UC Davis, maybe also Coursera?",
/* 21: GalaxyRise */		"[NOT IN USE] - it's linked to on the blog, that's enough",
/* 22: MetaScience */		"[NOT IN USE] - it's linked to on the blog, that's enough",
/* 23: Samaritans */		"Possibly?"
	);


	var printHTML = "<div id='Highlight'>" + highlightInfo[ID] + "</div>";

	$('div#Highlight').replaceWith(printHTML);
	if ($('#Highlight').css('display')=='none'){
                    $('#Highlight').fadeIn(600);
        } 

/*	document.getElementById("HighlightWrap").innerHTML=printHTML;*/
}



