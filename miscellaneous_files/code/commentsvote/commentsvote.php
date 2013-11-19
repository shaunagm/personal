<?php
/*
Plugin Name: Comments Vote
Plugin URI: http://www.bivings.com, http://www.shaunagm.net
Description: This plugin enables website users to vote comments up or 
down.  Reporting/moderating functionality added by Shauna GM.
Author: The Bivings Group, Shauna GM
Version: 2.0
Author URI: http://www.bivings.com/, http://www.shaunagm.net
*/

/*  Copyright 2008-2009 The Bivings Group (email : 
commentsvote@bivings.com)

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  
02110-1301  USA
*/

register_activation_hook( __FILE__, 'commentsvote_install' );

require_once( dirname( __FILE__) . '/commentsvote_inc.php' );

add_action( 'admin_menu', 'commentsvote_admin_menu' );
add_action( 'wp_head', 'commentsvote_js_header' );
add_action('admin_menu', 'commentsvote_handling_menu');


//----------------------------------------------------------------------

function commentsvote_handling_menu() {
  // Add a new sub-menu under comments
  add_comments_page( 'Flagged Comments', 'Flagged Comments', 
moderate_comments, 'CVHM', commentsvote_handling_function);
}

function commentsvote_handling_function() {

	 global $wpdb;
	 $cvTable = $wpdb->prefix . 'commentsvote';
         $wp_comments = $wpdb->prefix . 'wp_comments';

        // If comment-approve button has been pressed, changes database 
and redisplays
	if( isset($_POST[approve]) && $_POST[approve] == 'Approve 
Comment' ) {
                $comID =  $_POST[cID];        
		// The status of all votes in the table is set from 0 to 
1.
		$cvTable = $wpdb->prefix . 'commentsvote';
        	$rows_affected = $wpdb->query($wpdb->prepare("UPDATE 
$cvTable SET status=1 WHERE commentID=%d", $comID));

        	// Informs user
		echo "<b>**" . $comID . " has been approved.**</b><br 
/><br /><br />";
      }

	 echo "<b>Comments with one or more flags: </b><br />";
         echo "Delete comments through main moderator panel.  Approving 
comments permanently removes them from the flagged comments panel.<br 
/><br />";

         $flaggedcomments = $wpdb->get_results( $wpdb->prepare("SELECT 
DISTINCT commentID FROM $cvTable WHERE vote='-1' ORDER BY voteTime"));  
// 

	foreach ($flaggedcomments as $comment):

		$cID = $comment->commentID; 

		// Query to make sure it hasn't been resolved.
		$resolved = $wpdb->get_var( $wpdb->prepare("SELECT 
SUM(status) AS sum FROM $cvTable WHERE commentID=%d", $cID));

		// Query to make sure it hasn't been trashed.
		$trashed = $wpdb->get_var( $wpdb->prepare("SELECT 
$wpdb->comments.comment_approved FROM $wpdb->comments WHERE 
$wpdb->comments.comment_ID=%d", $cID));

		if (($resolved < 1) & ($trashed == 1))	// If not 
resolved/trashed
		{

  		$commentinfo = $wpdb->get_results( 
$wpdb->prepare("SELECT $wpdb->comments.comment_author, 
$wpdb->comments.comment_date, $wpdb->comments.comment_content FROM 
$wpdb->comments WHERE $wpdb->comments.comment_ID=%d", $cID));

                foreach ($commentinfo as $ci):
                	echo "<b>Comment " . $cID . "</b>  (<i>" . 
substr($ci->comment_content,0,40). "</i>)<br />";
			echo "<a href='" . get_comment_link( $cID, $args 
) . "'>This comment</a> written by " . $ci->comment_author . " at " . 
$ci->comment_date . ". <br />";
		endforeach;                  

                // Get info about flags
		$flaginfo = $wpdb->get_results( $wpdb->prepare("SELECT * 
FROM $cvTable WHERE commentID=%d", $cID));
		$logflag = 0;
		$unlogflag = 0;
		$logneg = 0;
		$unlogneg = 0;
                foreach ($flaginfo as $fi):
			if ($fi->userID == 0)
			{
			  $unlogflag = $unlogflag + 1;
			  if ($fi->vote == -1)
			  {
				$unlogneg = $unlogneg + 1;
			  }

			} else {
			  $logflag = $logflag + 1;
			  if ($fi->vote == -1)
			  {
				$logneg = $logneg + 1;
			  }
			}	

		endforeach;
		
		echo "There are " . ($logneg + $unlogneg) . " flags out 
of " . ($logflag + $unlogflag) . " total votes.";
		echo "  (" . $logneg . " from logged in users, " . 
$unlogneg . " from anonymous users.)<br />";

		//Comment handling ?>
		<form name="form1" method="post" action="">
		<input type="hidden" name="cID" value="<?php echo $cID; 
?>">
		<input type="submit" name="approve" 
class="button-secondary" value="Approve Comment" /></form><br />
		<?php
		}
	endforeach;



}

function commentsvote_admin_menu()
{
	add_options_page( 'Comments Vote', 'Comments Vote', 8, dirname( 
__FILE__ ) . '/commentsvote_admin.php' );
}

function commentsvote_js_header()
{
	global $commentsvotePath, $commentsvoteEnable;
	
	//Only fully enable the plugin when we're on a front-end page; 
the admin section doesn't call this function
	add_filter( 'get_comment_author_link', 'commentsvotePanel' );
	add_filter( 'comment_text', 'commentsvoteContent' );
	
	$commentsvotePath = $wp_object_cache->cache[ 'options' ][ 
'alloptions' ][ 'siteurl' ] . '/wp-content/plugins/commentsvote';
	
	wp_print_scripts( array( 'sack' ) );
	
	?>
	
	<link href="<?php echo $commentsvotePath; ?>/style.css" 
rel="stylesheet" type="text/css" />
	
	<script type="text/javascript">
	
	function votecomment( commentID, vote )
	{
		var mysack = new sack( "<?php echo $commentsvotePath; 
?>/commentsvote_ajax.php" );

		mysack.method = 'POST';
		
		mysack.setVar( 'vc_comment', commentID );
		mysack.setVar( 'vc_vote', vote );
		
		mysack.onError	= function() { alert( 'Voting error.' ) 
};
		mysack.onCompletion = function() { finishVote( 
commentID, eval( '(' + this.response + ')' )); }
		
		mysack.runAJAX();
	}
	
	function finishVote( commentID, response )
	{
		var currentVote	= response.votes;
		
		var vote_span_class	= '';
		var message = response.message;
		
		message	+= '<br />&nbsp;';

		if( currentVote > 0 )
		{
			currentVote	= '+' + currentVote;
			
			vote_span_class	= 'commentsvote_positive';
		}
		else if( currentVote < 0 )
		{
			vote_span_class	= 'commentsvote_negative';
			currentVote    = '';
		}
		else
		{
			currentVote	= '';
		}

		document.getElementById( 'commentsvote_span_' + 
commentID ).className = vote_span_class;

		document.getElementById( 'commentsvote_span_' + 
commentID ).innerHTML = currentVote;

		document.getElementById( 'commentsvote_results_div_' + 
commentID ).innerHTML = message;
	}
	
	</script>
	
	<?php
}

function commentsvotePanel($author)
{
	global $commentsvoteOptions, $commentsvotePath;
	global $comment;
	
	if( !isset( $commentsvoteOptions ) )
		$commentsvoteOptions = CVGetOptions();
	
	$votes = CVGetCommentVote($comment->comment_ID);
	$comment->_cv_vote = $votes;
	
	if( $votes == 0 || !$commentsvoteOptions[ 'display_rating' ] ) {
		$class = '';
		$votes = '';
	} else if($votes < 0) {
		$class = '';
		$votes = '';
	} else {
		$class = 'commentsvote_positive';
		
		$votes = '+' . $votes;
	}

	$results = '<div id="commentsvote_results_div_' . 
$comment->comment_ID . '"></div> <span class="' . $class . '" 
id="commentsvote_span_' . $comment->comment_ID . '">' . $votes . 
'</span>    ' . $author . '   <a href="javascript:void(0);" 
onclick="votecomment( ' . $comment->comment_ID . ', 1 );" title="Vote 
+1">(like) </a> <a href="javascript:void(0);" onclick="votecomment( ' . 
$comment->comment_ID . ', -1 );" title="flag this comment"><b><i>  
(flag)  </i></b></a>';
		
	return $results;
}

function commentsvoteContent($content)
{
	global $commentsvoteOptions;
	global $comment;
	
	if( !isset( $commentsvoteOptions ) )
		$commentsvoteOptions = CVGetOptions();
	
	$hideComment = ($commentsvoteOptions[ 'threshold' ] > 0 && ( 
$comment->_cv_vote <= -$commentsvoteOptions[ 'threshold' ] ) );
	
	if( $hideComment ) {
		$content = '<a href="javascript:void(0);" 
onclick="if(document.getElementById(\'hidden_comment_' . 
$comment->comment_ID . 
'\').style.display==\'block\'){document.getElementById(\'hidden_comment_' 
. $comment->comment_ID . 
'\').style.display=\'none\';}else{document.getElementById(\'hidden_comment_' 
. $comment->comment_ID . '\').style.display=\'block\';}">(This comment 
has been flagged for moderation.)</a><div id="hidden_comment_' . 
$comment->comment_ID . '" style="display:none;"><p>' . $content . 
'</p></div>';
	}
	
	return $content;
}

function commentsvote_install()
{
	global $wpdb;
	
	$dbVersion = get_option('commentsvote_db_version');
	
	if( $dbVersion < 1 )
	{
		$cvTable = $wpdb->prefix . 'commentsvote';
		$wpdb->query( "CREATE TABLE $cvTable (
			id INT UNSIGNED NOT NULL AUTO_INCREMENT,
			commentID INT UNSIGNED NOT NULL,
			userID INT UNSIGNED NOT NULL,
			vote TINYINT(1) NOT NULL,
			ip INT UNSIGNED NOT NULL,
			voteTime INT UNSIGNED NOT NULL,
			status TINYINT(4) NOT NULL,
			reason TINYINT(4) NOT NULL,
			UNIQUE KEY (id),
			INDEX (commentID, userID),
			INDEX (commentID, ip)
			)"
		);
		
		add_option( 'commentsvote_db_version', 1 );
		add_option( 'commentsvote_display_rating', 1 );
		add_option( 'commentsvote_threshold', 0 );
		add_option( 'commentsvote_require_login', 0 );
	}
}

?>

