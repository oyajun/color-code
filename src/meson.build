pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'color_code'
gnome = import('gnome')

blueprints = custom_target('blueprints',
  input: files(
    'window.blp',
    'gtk/help-overlay.blp',
    'page_4_bands.blp',
    'page_5_bands.blp',
    'page_6_bands.blp',
    'drop_down_value.blp',
    'drop_down_multiplier.blp',
    'drop_down_tolerance.blp',
    'drop_down_tcr.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

gnome.compile_resources('color-code',
  'color-code.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
  dependencies: blueprints,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'color-code.in',
  output: 'color-code',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

color_code_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'utils.py',
  'page_4_bands.py',
  'page_5_bands.py',
  'page_6_bands.py',
  'drop_down_value.py',
  'drop_down_multiplier.py',
  'drop_down_tolerance.py',
  'drop_down_tcr.py',
  'colors.py',
]

install_data(color_code_sources, install_dir: moduledir)
