<?php
if (!defined('ABSPATH')) { exit; }
get_header();
$id = get_the_ID();
$outcomes = cm_project_meta($id, 'cm_outcomes');
$steps = cm_project_meta($id, 'cm_steps');
?>
<main class="cm-content-wrap">
  <article class="cm-single">
    <div class="section-kicker">SERVICE / <?php echo esc_html(cm_project_meta($id, 'cm_service_label', 'COMMERCE SYSTEMS')); ?></div>
    <h1><?php the_title(); ?></h1>
    <div class="cm-copy"><?php the_content(); ?></div>
    <?php if ($outcomes) : ?>
      <h2>ما الذي تحصل عليه؟</h2>
      <ul>
        <?php foreach (preg_split('/\r\n|\r|\n/', $outcomes) as $item) : if (trim($item) !== '') : ?>
          <li><?php echo esc_html($item); ?></li>
        <?php endif; endforeach; ?>
      </ul>
    <?php endif; ?>
    <?php if ($steps) : ?>
      <h2>طريقة العمل</h2>
      <div class="cm-service-grid">
        <?php foreach (preg_split('/\r\n|\r|\n/', $steps) as $step) : if (trim($step) !== '') : $parts = explode('—', $step, 2); ?>
          <div class="cm-card"><span class="cm-meta">STEP</span><h3><?php echo esc_html(trim($parts[0])); ?></h3><p><?php echo esc_html(trim(isset($parts[1]) ? $parts[1] : '')); ?></p></div>
        <?php endif; endforeach; ?>
      </div>
    <?php endif; ?>
    <p><a class="button primary" href="<?php echo esc_url(home_url('/#contact')); ?>">ابدأ من الـBrief ←</a></p>
  </article>
</main>
<?php get_footer(); ?>
