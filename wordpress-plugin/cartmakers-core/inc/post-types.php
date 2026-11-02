<?php
if (!defined('ABSPATH')) { exit; }
function cm_register_post_types() {
    register_post_type('cm_project', [
        'labels' => ['name'=>'Portfolio Projects','singular_name'=>'Portfolio Project','add_new_item'=>'Add Portfolio Project','edit_item'=>'Edit Portfolio Project'],
        'public'=>true,'show_in_rest'=>true,'menu_icon'=>'dashicons-portfolio','supports'=>['title','editor','thumbnail','excerpt','page-attributes'],'has_archive'=>false,'rewrite'=>['slug'=>'projects','with_front'=>false],
    ]);
    register_taxonomy('cm_project_category','cm_project',['labels'=>['name'=>'Project Categories'],'public'=>true,'show_in_rest'=>true,'hierarchical'=>true,'rewrite'=>['slug'=>'project-category']]);
    register_post_type('cm_service', [
        'labels'=>['name'=>'Services','singular_name'=>'Service','add_new_item'=>'Add Service','edit_item'=>'Edit Service'],
        'public'=>true,'show_in_rest'=>true,'menu_icon'=>'dashicons-admin-tools','supports'=>['title','editor','thumbnail','excerpt','page-attributes'],'has_archive'=>'services','rewrite'=>['slug'=>'services','with_front'=>false],
    ]);
    register_post_type('cm_testimonial', [
        'labels'=>['name'=>'Testimonials','singular_name'=>'Testimonial','add_new_item'=>'Add Testimonial','edit_item'=>'Edit Testimonial'],
        'public'=>false,'show_ui'=>true,'show_in_rest'=>true,'menu_icon'=>'dashicons-format-quote','supports'=>['title','editor','thumbnail','page-attributes'],
    ]);
}
add_action('init','cm_register_post_types');
