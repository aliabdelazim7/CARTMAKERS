<?php
if (!defined('ABSPATH')) { exit; }
function cm_meta_boxes() {
    add_meta_box('cm_project_details','Project Details','cm_project_box','cm_project','normal','high');
    add_meta_box('cm_service_details','Service Details','cm_service_box','cm_service','normal','high');
    add_meta_box('cm_testimonial_details','Testimonial Details','cm_testimonial_box','cm_testimonial','normal','high');
}
add_action('add_meta_boxes','cm_meta_boxes');
function cm_field($label,$name,$value,$type='text') { printf('<p><label><strong>%s</strong></label><br><input class="widefat" type="%s" name="%s" value="%s"></p>',esc_html($label),esc_attr($type),esc_attr($name),esc_attr($value)); }
function cm_textarea($label,$name,$value) { printf('<p><label><strong>%s</strong></label><br><textarea class="widefat" rows="4" name="%s">%s</textarea></p>',esc_html($label),esc_attr($name),esc_textarea($value)); }
function cm_project_box($post) {
    wp_nonce_field('cm_save_meta','cm_meta_nonce');
    foreach ([['External project URL','cm_external_url'],['Category label','cm_category_label'],['Short tag','cm_tag'],['Platform','cm_platform']] as $f) cm_field($f[0],$f[1],get_post_meta($post->ID,$f[1],true));
    cm_textarea('Project brief','cm_brief',get_post_meta($post->ID,'cm_brief',true));
    cm_textarea('Project insight','cm_insight',get_post_meta($post->ID,'cm_insight',true));
    cm_textarea('Features (one per line)','cm_features',get_post_meta($post->ID,'cm_features',true));
}
function cm_service_box($post) {
    wp_nonce_field('cm_save_meta','cm_meta_nonce');
    cm_field('Service label','cm_service_label',get_post_meta($post->ID,'cm_service_label',true));
    cm_textarea('Outcomes (one per line)','cm_outcomes',get_post_meta($post->ID,'cm_outcomes',true));
    cm_textarea('Steps (one per line; title — description)','cm_steps',get_post_meta($post->ID,'cm_steps',true));
}
function cm_testimonial_box($post) {
    wp_nonce_field('cm_save_meta','cm_meta_nonce');
    foreach ([['Client name','cm_client_name'],['Brand','cm_client_brand'],['Rating','cm_rating','number'],['Approved for publishing (yes/no)','cm_approved']] as $f) cm_field($f[0],$f[1],get_post_meta($post->ID,$f[1],true),$f[2]??'text');
}
function cm_save_meta($post_id) {
    if (!isset($_POST['cm_meta_nonce']) || !wp_verify_nonce(sanitize_text_field(wp_unslash($_POST['cm_meta_nonce'])),'cm_save_meta')) return;
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) return;
    if (!current_user_can('edit_post',$post_id)) return;
    $keys=['cm_external_url','cm_category_label','cm_tag','cm_platform','cm_brief','cm_insight','cm_features','cm_service_label','cm_outcomes','cm_steps','cm_client_name','cm_client_brand','cm_rating','cm_approved'];
    foreach($keys as $key){ if(isset($_POST[$key])) update_post_meta($post_id,$key,sanitize_textarea_field(wp_unslash($_POST[$key]))); }
}
add_action('save_post','cm_save_meta');
