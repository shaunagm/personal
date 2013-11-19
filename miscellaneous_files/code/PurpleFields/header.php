<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head profile="http://gmpg.org/xfn/11">



	<title><?php bloginfo('name'); ?><?php wp_title(); ?></title>



	<meta http-equiv="Content-Type" content="<?php bloginfo('html_type'); ?>; charset=<?php bloginfo('charset'); ?>" />	

	<meta name="generator" content="WordPress <?php bloginfo('version'); ?>" /> <!-- leave this for stats please -->



	<link rel="stylesheet" href="<?php bloginfo('stylesheet_url'); ?>" type="text/css" media="screen" />

	<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="<?php bloginfo('rss2_url'); ?>" />

	<link rel="alternate" type="text/xml" title="RSS .92" href="<?php bloginfo('rss_url'); ?>" />

	<link rel="alternate" type="application/atom+xml" title="Atom 0.3" href="<?php bloginfo('atom_url'); ?>" />

	<link rel="pingback" href="<?php bloginfo('pingback_url'); ?>" />



	<?php wp_get_archives('type=monthly&format=link'); ?>

	<?php //comments_popup_script(); // off by default ?>

	<?php wp_head(); ?>

</head>

<body>

<div id="wrapper">

<div id="header">
<div id="treewrap">
	<div id="pushtree">

	</div>
	<div id="centertree">
		<h1><a href="<?php bloginfo('url'); ?>"><?php bloginfo("name"); ?></a></h1>
		<h3><?php bloginfo("description"); ?></h3>
	</div>
</div>
	<div id="righttree">
		<?php
		$args = array( "meta_key" => 'showintree', "meta_value" => '2' );
		$values = get_pages($args); 
		$order = 0;
		foreach($values as $post ) : setup_postdata($post); 
			if ($order == 0) {
			?>
				<div id="firstlink"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></div>
			<?php
				$order = $order + 1;
			} else {
			?>
				<div id="secondlink"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></div>
			<?php
			}
?>
		
<?php endforeach; ?>
		
	
	</div>

		
</div>

<div id="main">
