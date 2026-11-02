<?php
if (!defined('ABSPATH')) { exit; }

if (!function_exists('cm_settings_defaults')) {
    function cm_settings_defaults() {
        return array(
            'email' => 'contact@cart-makers.com',
            'whatsapp' => '201558334626',
            'facebook' => 'https://www.facebook.com/cart.makerss/',
            'instagram' => 'https://www.instagram.com/cart.makers/',
            'tiktok' => 'https://www.tiktok.com/@cart.makers',
            'hero_title' => 'من أول Click لحد Repeat Purchase.',
            'hero_description' => 'بنحوّل الطلب المتناثر من السوشيال والـMarketplace إلى نظام تجارة يبيع، يتتبع، ويتحسن — من غير وعود وهمية.',
            'primary_color' => '#101828',
            'accent_color' => '#C7F36B',
            'telegram_token' => '',
            'telegram_chat_id' => '',
        );
    }
}
if (!function_exists('cm_settings')) {
    function cm_settings() {
        return wp_parse_args(get_option('cm_settings', array()), cm_settings_defaults());
    }
}
function cm_register_settings() {
    register_setting('cm_settings_group', 'cm_settings', array('sanitize_callback' => 'cm_sanitize_settings'));
    add_settings_section('cm_brand_section', 'CartMakers Global Settings', function () {
        echo '<p>Edit the website identity and contact details here. Secrets are optional and never printed publicly.</p>';
    }, 'cm-settings');
    foreach (cm_settings_defaults() as $key => $default) {
        add_settings_field('cm_' . $key, ucwords(str_replace('_', ' ', $key)), 'cm_setting_field', 'cm-settings', 'cm_brand_section', array('key' => $key));
    }
}
add_action('admin_init', 'cm_register_settings');
function cm_sanitize_settings($input) {
    $input = is_array($input) ? $input : array();
    $out = cm_settings_defaults();
    foreach ($out as $key => $default) {
        if (!isset($input[$key])) { continue; }
        if ($key === 'email') { $out[$key] = sanitize_email($input[$key]); }
        elseif ($key === 'hero_description' || $key === 'hero_title') { $out[$key] = sanitize_textarea_field($input[$key]); }
        else { $out[$key] = sanitize_text_field($input[$key]); }
    }
    return $out;
}
function cm_setting_field($args) {
    $settings = cm_settings();
    $key = isset($args['key']) ? $args['key'] : '';
    $type = ($key === 'telegram_token' || $key === 'telegram_chat_id') ? 'password' : 'text';
    printf('<input class="regular-text" type="%s" name="cm_settings[%s]" value="%s">', esc_attr($type), esc_attr($key), esc_attr(isset($settings[$key]) ? $settings[$key] : ''));
}
function cm_settings_menu() { add_options_page('CartMakers Settings', 'CartMakers Settings', 'manage_options', 'cm-settings', 'cm_settings_page'); }
add_action('admin_menu', 'cm_settings_menu');
function cm_settings_page() {
    if (!current_user_can('manage_options')) { return; }
    ?><div class="wrap"><h1>CartMakers Settings</h1><form method="post" action="options.php"><?php settings_fields('cm_settings_group'); do_settings_sections('cm-settings'); submit_button(); ?></form><p><strong>WhatsApp:</strong> Use international digits only, e.g. 201558334626.</p></div><?php
}
