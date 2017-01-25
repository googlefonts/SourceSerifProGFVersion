import os

REMAP_FONTS = [
    ('SourceSerifPro-Black.ttf', 'SourceSerifPro-Black.ttf.renamed'),
    ('SourceSerifPro-Bold.ttf', 'SourceSerifPro-Bold.ttf.renamed'),
    ('SourceSerifPro-ExtraLight.ttf', 'SourceSerifPro-ExtraLight.ttf.renamed'),
    ('SourceSerifPro-Light.ttf', 'SourceSerifPro-Light.ttf.renamed'),
    ('SourceSerifPro-Regular.ttf', 'SourceSerifPro-Regular.ttf.renamed'),
    ('SourceSerifPro-Semibold.ttf', 'SourceSerifPro-SemiBold.ttf.renamed'),
]

for old_name, new_name in REMAP_FONTS:
    if old_name in os.listdir('.'):
        os.rename(os.path.join('.', old_name), os.path.join('.', new_name))
        print 'ttf.renamed %s to %s' % (old_name, new_name)
print 'Done renaming'
