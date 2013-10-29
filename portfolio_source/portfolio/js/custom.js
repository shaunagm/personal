/// <reference path="path-to-vsdoc-file" />

function highlight(ID) {

	// This function creates an array of information.  When an item from the grid is selected, the information is displayed in
	// the "Highlight" div.

	var highlightInfo = new Array(
/* 0: Personal Blog */		"I've kept a regularly updated personal blog since January 2010.<br /><br />My favorite posts include:<br /><a href='http://www.shaunagm.net/blog/2013/10/hacking-the-hackathon/' target='_blank'>Hacking the Hackathon</a><br /><a href='http://www.shaunagm.net/blog/2013/02/how-to-find-a-statistically-significant-other/' target='_blank'>How to Find a Statistically Significant Other</a><br /><a href='http://www.shaunagm.net/blog/2011/02/greatness-and-depression/' target='_blank'>Lincoln's Inner War</a>",
/* 1: OpenHatch Blog */		"OpenHatch Blog [time (? to present); include list of favorite posts, mention I came up with IAQs]",
/* 2: OSC Blog */		"OSC Blog [time (? to present); say what it is and what I do for it]",
/* 3: Fiction */		"I've been writing most of my life, but I've only started trying to publish recently, so I have exactly one published piece:<br /><br /><a href='http://issue.liquid-imagination.com/article/hibernation-by-shauna-gordon-mckeon/' target='_blank'>Hibernation</a>, published 2/2013 in Liquid Imagination<br /><br />I also have a few pieces I have no plan on publishing, which I've released under a CC-BY-SA license:<br /><br />Silence - a retelling of the Little Mermaid<br />The Cry of the Crow – historical fiction set around 2380 BC, centering on Urukagina of Lagash<br /><br />You can also browse through <a href='http://www.shaunagm.net/blog/writing/' target='_blank'>blog posts tagged writing</a>.",
/* 4: Web Des & Dv */		"I have done a small amount of freelance and volunteer web development, mostly using Wordpress.  My work includes:<br /><br /><a href=''>Purple Fields</a> Wordpress theme<br /><br />Shulamis publicity site (<a href=''>screenshots</a>)<br /><br /> <a href=''>adapted Comments Vote plugin</a> for The Hathor Legacy<br /><br /> a Wordpress website for <a href='http://childrenscharter.org/'>Children's Charter</a> built during a hackathon (not their current site) <br /><br />and this portfolio page, built using the <a href='http://mixitup.io/'>MixItUp</a> plugin<br />",
/* 5: MediaLab */		"Media Lab [dates, responsibilities]",
/* 6: Laser Lab */		"Laser Lab [dates, responsibilities]",
/* 7: OpenHatch */		"OpenHatch [dates, responsibilites], link to OH blog",
/* 8: Parts & Crafts */		"Parts & Crafts [dates, responsibilities], link to P+C materials on github",
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
/* 19: TA CogNeuro */		"I TA'd cognitive neuroscience.  yup.",
/* 20: Non-degree CW */		"Harvard Extension? Coursera? SCCC?) ?",
/* 21: GalaxyRise */		"Possibly?  It's linked to on the blog.",
/* 22: MetaScience */		"Possibly?  It's linked to on the blog.",
/* 23: Samaritans */		"Possibly?"
	);


	var printHTML = "<div id='Highlight'>" + highlightInfo[ID] + "</div>";

	$('div#Highlight').replaceWith(printHTML);
	if ($('#Highlight').css('display')=='none'){
                    $('#Highlight').fadeIn(600);
        } 

/*	document.getElementById("HighlightWrap").innerHTML=printHTML;*/
}



