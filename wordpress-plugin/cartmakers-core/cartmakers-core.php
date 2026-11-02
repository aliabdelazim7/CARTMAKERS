<?php
/**
 * Plugin Name: CartMakers Core
 * Description: Portable content, settings, portfolio, services, testimonials and contact functionality for the CartMakers theme.
 * Version: 1.0.0
 * Author: CartMakers
 * Text Domain: cartmakers-core
 */
if (!defined('ABSPATH')) { exit; }

define('CM_CORE_VERSION', '1.0.0');
define('CM_CORE_DIR', plugin_dir_path(__FILE__));

require_once CM_CORE_DIR . 'inc/post-types.php';
require_once CM_CORE_DIR . 'inc/meta-boxes.php';
require_once CM_CORE_DIR . 'inc/settings.php';
require_once CM_CORE_DIR . 'inc/importer.php';
require_once CM_CORE_DIR . 'inc/contact.php';

register_activation_hook(__FILE__, function () {
    cm_register_post_types();
    flush_rewrite_rules();
});
register_deactivation_hook(__FILE__, 'flush_rewrite_rules');
