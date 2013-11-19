<div class="sidebar">

	<ul>

		<?php if ( function_exists('dynamic_sidebar') && dynamic_sidebar() ) : else : ?>

		<?php wp_list_pages('title_li=<h2>Pages</h2>'); ?>

		<li class="listheaders"><h2><?php _e('Categories'); ?></h2>
			<ul class="listcontent">
				<?php wp_list_cats('sort_column=name&optioncount=1&hierarchical=0'); ?>
			</ul>
		</li>

		<li class="listheaders"><h2><?php _e('Archives'); ?></h2>
			<ul class="listcontent">
				<?php wp_get_archives('type=monthly'); ?>
			</ul>
		</li>

		<?php wp_list_bookmarks('title_li=<h2>Blogroll</h2>&class=linkcat2'); ?>

		<li class="listheaders"><h2><?php _e('Meta'); ?></h2>
			<ul class="listcontent">
				<?php wp_register(); ?>
				<li><?php wp_loginout(); ?></li>
				<?php wp_meta(); ?>
			</ul>
		</li>
	
		<?php endif; ?>
	</ul>

</div>
