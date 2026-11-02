<?php
if (!defined('ABSPATH')) { exit; }
define('CM_THEME_VERSION','1.0.0');
if (!function_exists('cm_settings_defaults')) { function cm_settings_defaults(){return ['email'=>'contact@cart-makers.com','whatsapp'=>'201558334626','facebook'=>'https://www.facebook.com/cart.makerss/','instagram'=>'https://www.instagram.com/cart.makers/','tiktok'=>'https://www.tiktok.com/@cart.makers','hero_title'=>'من أول Click لحد Repeat Purchase.','hero_description'=>'بنحوّل الطلب المتناثر من السوشيال والـMarketplace إلى نظام تجارة يبيع، يتتبع، ويتحسن — من غير وعود وهمية.','primary_color'=>'#101828','accent_color'=>'#C7F36B'];} }
if (!function_exists('cm_settings')) { function cm_settings(){return cm_settings_defaults();} }
function cm_theme_setup(){load_theme_textdomain('cartmakers-theme',get_template_directory().'/languages');add_theme_support('title-tag');add_theme_support('post-thumbnails');add_theme_support('html5',['search-form','comment-form','comment-list','gallery','caption','style','script']);add_theme_support('custom-logo',['height'=>80,'width'=>360,'flex-width'=>true]);register_nav_menus(['primary'=>'Primary Navigation','footer'=>'Footer Navigation']);}
add_action('after_setup_theme','cm_theme_setup');
function cm_assets(){wp_enqueue_style('cartmakers-style',get_stylesheet_uri(),[],CM_THEME_VERSION);wp_enqueue_script('cartmakers-theme',get_template_directory_uri().'/assets/js/cartmakers-theme.js',[],CM_THEME_VERSION,true);}
add_action('wp_enqueue_scripts','cm_assets');
function cm_body_classes($classes){$classes[]='cartmakers-wp';return $classes;} add_filter('body_class','cm_body_classes');
function cm_option($key,$fallback=''){ $s=function_exists('cm_settings')?cm_settings():[];return isset($s[$key])&&$s[$key]!==''?$s[$key]:$fallback; }
function cm_image_url($post_id){$url=get_the_post_thumbnail_url($post_id,'large');return $url?:get_template_directory_uri().'/assets/images/velora.webp';}
function cm_project_meta($id,$key,$fallback=''){ $v=get_post_meta($id,$key,true);return $v!==''?$v:$fallback; }
function cm_excerpt_text($post,$fallback=''){return has_excerpt($post)?get_the_excerpt($post):wp_trim_words(wp_strip_all_tags($post->post_content),28,'…')?:$fallback;}
function cm_head_meta(){if(is_singular()){global $post;$desc=cm_excerpt_text($post,get_bloginfo('description'));if($desc){echo '<meta name="description" content="'.esc_attr($desc).'">';} $img=get_the_post_thumbnail_url($post,'large');if($img)echo '<meta property="og:image" content="'.esc_url($img).'">';} }
add_action('wp_head','cm_head_meta',2);
function cm_schema(){if(is_front_page()){ $org=['@context'=>'https://schema.org','@type'=>'Organization','@id'=>home_url('/').'#organization','name'=>'CartMakers','alternateName'=>['Cart Makers','كارت ميكرز'],'url'=>home_url('/'),'logo'=>get_template_directory_uri().'/assets/cartmakers-new-logo.webp','email'=>cm_option('email','contact@cart-makers.com'),'sameAs'=>[cm_option('facebook'),cm_option('instagram'),cm_option('tiktok')]];echo '<script type="application/ld+json">'.wp_json_encode($org).'</script>';}}
add_action('wp_head','cm_schema',20);
function cm_customizer($wp_customize){$wp_customize->add_section('cm_brand',['title'=>'CartMakers Brand','priority'=>30]);foreach(['primary_color'=>'Primary color','accent_color'=>'Accent color'] as $key=>$label){$wp_customize->add_setting($key,['default'=>cm_settings_defaults()[$key],'sanitize_callback'=>'sanitize_hex_color']);$wp_customize->add_control(new WP_Customize_Color_Control($wp_customize,$key,['label'=>$label,'section'=>'cm_brand']));}}
add_action('customize_register','cm_customizer');
function cm_inline_brand(){ $s=cm_settings();echo '<style>:root{--ink:'.esc_attr($s['primary_color']).';--lime:'.esc_attr($s['accent_color']).'}</style>'; }
add_action('wp_head','cm_inline_brand',30);
