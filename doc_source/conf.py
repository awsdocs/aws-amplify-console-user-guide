# -*- coding: utf-8 -*-
#
# AWS Sphinx configuration file.
#
# For more information about how to configure this file, see:
#
# https://w.amazon.com/index.php/AWSDevDocs/Sphinx
#

#
# General information about the project.
#

# The long version of the service or SDK name, such as "Amazon Simple Workflow
# Service", "AWS Flow Framework for Ruby" or "AWS SDK for Java"
service_name_long = u'AWS Amplify'
service_docs_home = u'http://aws.amazon.com/documentation/amplify/'

project = u'Console User Guide'
project_desc = u'AWS Amplify Console User Guide'
project_basename = u'amplify/userguide'

# This name is used as the manual / PDF name. Don't include the extension
# (.pdf) here.
man_name = u'amplify-console-ug'

# Optional forum ID. If there's a relevant forum at forums.aws.amazon.com, then
# set the ID here. If not set, then no forum ID link will be generated.
forum_id = u'314'

# For the url docs.aws.amazon.com/docset-root/version/guide-name
docset_path_slug = u'amplify'
version_path_slug = u'latest'
guide_path_slug = u'userguide'

build_html = True
build_pdf = True
build_mobi = False #Or the Kindle ASIN if you need a Kindle build

feedback_name = u'Amplify'

extra_navlinks = []

# The link to the top of the doc source tree on GitHub. This allows generation
# of per-page "Edit on GitHub" links.
github_doc_url = 'https://github.com/awsdocs/aws-amplify-console-user-guide/tree/master/doc_source'

# EXTRA_CONF_CONTENT -- don't change, move or remove this line!
