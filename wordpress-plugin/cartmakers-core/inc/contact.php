<?php
if (!defined('ABSPATH')) { exit; }
function cm_contact_redirect($status){$url=wp_get_referer()?:home_url('/');wp_safe_redirect(add_query_arg('cm_contact',$status,$url));exit;}
function cm_handle_contact(){
    if($_SERVER['REQUEST_METHOD']!=='POST'||!isset($_POST['cm_contact_nonce'])||!wp_verify_nonce(sanitize_text_field(wp_unslash($_POST['cm_contact_nonce'])),'cm_contact'))cm_contact_redirect('error');
    if(!empty($_POST['website']))cm_contact_redirect('success');
    $name=sanitize_text_field(wp_unslash($_POST['name']??''));$email=sanitize_email(wp_unslash($_POST['email']??''));$phone=sanitize_text_field(wp_unslash($_POST['phone']??''));$message=sanitize_textarea_field(wp_unslash($_POST['message']??''));
    if(!$name||!is_email($email)||!$message)cm_contact_redirect('missing');
    $s=cm_settings();$subject='New CartMakers Brief — '.$name;$body="Name: {$name}\nEmail: {$email}\nPhone: {$phone}\n\nBrief:\n{$message}";
    $sent=wp_mail(get_option('admin_email'),$subject,$body,['Reply-To: '.$email]);
    if(!empty($s['telegram_token'])&&!empty($s['telegram_chat_id'])){wp_remote_post('https://api.telegram.org/bot'.rawurlencode($s['telegram_token']).'/sendMessage',['timeout'=>8,'body'=>['chat_id'=>$s['telegram_chat_id'],'text'=>$body]]);}
    cm_contact_redirect($sent?'success':'error');
}
add_action('admin_post_nopriv_cm_contact','cm_handle_contact');add_action('admin_post_cm_contact','cm_handle_contact');
