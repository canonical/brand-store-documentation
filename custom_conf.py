import datetime
import logging
import os
import sys
import yaml

sys.path.append(os.path.abspath("./_ext"))
logger = logging.getLogger()
# Custom configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# The file is included in the common conf.py configuration file.
# You can modify any of the settings below or add any configuration that
# is not covered by the common conf.py file.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

############################################################
### Project information
############################################################

# Product name
html_title = full_title = project = 'Canonical Brand Store'
author = 'Canonical Group Ltd'

# Uncomment if your product uses release numbers
# release = '1.0'

# The default value uses the current year as the copyright year
copyright = '%s, %s' % (datetime.date.today().year, author)

## Open Graph configuration - defines what is displayed in the website preview
# The URL of the documentation output
ogp_site_url = 'https://canonical-starter-pack.readthedocs-hosted.com/'
# The documentation website name (usually the same as the product name)
ogp_site_name = project
# An image or logo that is used in the preview
ogp_image = 'https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg'

# Update with the favicon for your product (default is the circle of friends)
html_favicon = '.sphinx/_static/favicon.png'

# (Some settings must be part of the html_context dictionary, while others
#  are on root level. Don't move the settings.)
html_context = {

    # Change to the link to your product website (without "https://")
    'product_page': 'documentation.ubuntu.com',

    # Add your product tag to ".sphinx/_static" and change the path
    # here (start with "_static"), default is the circle of friends
    'product_tag': '_static/tag.png',

    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    'discourse': 'https://discourse.ubuntu.com',

    # Change to the GitHub info for your project
    'github_url': 'https://github.com/canonical/brand-store-documentation',

    # Change to the branch for this version of the documentation
    'github_version': 'main',

    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    'github_folder': '/',

    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    'github_issues': 'enabled',
}

# If your project is on documentation.ubuntu.com, specify the project
# slug (for example, "lxd") here.
slug = ""

############################################################
### Redirects
############################################################

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: 'explanation/old-name.html': '../how-to/prettify.html',

redirects = {}

############################################################
### Link checker exceptions
############################################################

# Links to ignore when checking links

linkcheck_ignore = [
    'http://127.0.0.1:8000',
    'https://readthedocs.com/projects/canonical-canonical-brand-store/',
    'https://dashboard.snapcraft.io/reviewer/{{CUSTOMER_STORE_ID}}/',
]

############################################################
### Additions to default configuration
############################################################

## The following settings are appended to the default configuration.
## Use them to extend the default functionality.

# Add extensions
custom_extensions = ['rstjinja', 'better-term']

# Add files or directories that should be excluded from processing.
custom_excludes = ['WORKFLOW.rst']

# Add CSS files (located in .sphinx/_static/)
custom_html_css_files = []

# Add JavaScript files (located in .sphinx/_static/)
custom_html_js_files = []

## The following settings override the default configuration.

# Specify a reST string that is included at the end of each file.
# If commented out, use the default (which pulls the reuse/links.txt
# file into each reST file).
# custom_rst_epilog = ''

# By default, the documentation includes a feedback button at the top.
# You can disable it by setting the following configuration to True.
disable_feedback_button = False

############################################################
### Additional configuration
############################################################

## Add any configuration that is not covered by the common conf.py file.

# Load default values for template variables, used when no TEMPLATE_FILENAME is
# specified.
template_values = {}
with open("templates/TEMPLATE.yaml") as template_file:
    template_values = yaml.safe_load(template_file)

try:
    with open(os.environ['TEMPLATE_FILENAME']) as template_file:
        template_values = yaml.safe_load(template_file)
except:
    # Fallback to the defaults
    pass

# Merge the template values with the HTML context so the documentation can use
# template variables.
html_context = {**html_context, **template_values}

latex_engine = 'xelatex'
# This whole thing is a hack and a half, but it works.
latex_elements = {
    'pointsize': '11pt',
    'fncychap': '',
    'preamble': r'''
%\usepackage{charter}
%\usepackage[defaultsans]{lato}
%\usepackage{inconsolata}
\setmainfont[Path = ../../fonts/, UprightFont = *-R, BoldFont = *-B, ItalicFont=*-RI]{Ubuntu}
\setmonofont[Path = ../../fonts/, UprightFont = *-R]{UbuntuMono}
\usepackage[most]{tcolorbox}
\tcbuselibrary{breakable}
\usepackage{lastpage}
\usepackage{tabto}
\usepackage{ifthen}
\usepackage{etoolbox}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{titlesec}
\graphicspath{ {../../images/} }
\definecolor{yellowgreen}{RGB}{154, 205, 50}
\definecolor{title}{RGB}{76, 17, 48}
\definecolor{subtitle}{RGB}{116, 27, 71}
\definecolor{label}{RGB}{119, 41, 100}
\definecolor{copyright}{RGB}{174, 167, 159}
\makeatletter
\def\tcb@finalize@environment{%
  \color{.}% hack for xelatex
  \tcb@layer@dec%
}
\makeatother
\newenvironment{sphinxclassprompt}{\color{yellowgreen}}{}
\tcbset{colback=black, fontupper=\color{white}}
\newtcolorbox{termbox}{breakable, colupper=white}
\newenvironment{sphinxclassterminal}{\color{white}\sphinxsetup{VerbatimColor={black}}\begin{termbox}}{\end{termbox}}
\newcommand{\dimtorightedge}{%
  \dimexpr\paperwidth-1in-\hoffset-\oddsidemargin\relax}
\newcommand{\dimtotop}{%
  \dimexpr\height-1in-\voffset-\topmargin-\headheight-\headsep\relax}
\newtoggle{tpage}
\AtBeginEnvironment{titlepage}{\global\toggletrue{tpage}}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[R]{\thepage\ of \pageref*{LastPage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{normal}{
    \fancyhf{}
    \fancyfoot[R]{\thepage\ of \pageref*{LastPage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{titlepage}{%
    \fancyhf{}
    \fancyfoot[L]{\footnotesize \textcolor{copyright}{© 2023 Canonical Ltd. All rights reserved. \newline Confidential and proprietary, do not share without permission.}}
}
\newcommand\sphinxbackoftitlepage{\thispagestyle{titlepage}}
\titleformat{\chapter}[block]{\Huge \color{title} \bfseries\filright}{\thechapter .}{1.5ex}{}
\titlespacing{\chapter}{0pt}{0pt}{0pt}
\titleformat{\section}[block]{\huge \bfseries\filright}{\thesection .}{1.5ex}{} 
\titlespacing{\section}{0pt}{0pt}{0pt}
\titleformat{\subsection}[block]{\Large \bfseries\filright}{\thesubsection .}{1.5ex}{} 
\titlespacing{\subsection}{0pt}{0pt}{0pt}
\setcounter{tocdepth}{1}
\renewcommand\pagenumbering[1]{}
''',
    'sphinxsetup': 'verbatimwithframe=false, pre_border-radius=0pt, verbatimvisiblespace=\\phantom{}, verbatimcontinued=\\phantom{}',
    'extraclassoptions': 'openany,oneside',
    'maketitle': r'''
\begin{titlepage}
\begin{flushleft}
        \hbox
        {%
            \makebox[\dimtorightedge]{}%
            \makebox[0pt][r]
            {\raisebox{0pt}[\dimtotop]{\includegraphics[width=\paperwidth]{title-page-header}}}%
        }
\end{flushleft}
\Huge \textcolor{title}{''' + template_values['CUSTOMER_NAME'] + r''' Onboarding Guide}

\Large \textcolor{subtitle}{\textit{Brand Store and Image Build Quick-Start Guide}}

\vfill

\textcolor{label}{Prepared by:} \tabto{8em} ''' + template_values['PREPARED_BY'] + r'''

\textcolor{label}{Prepared on:} \tabto{8em} ''' + template_values['PREPARED_ON'] + r'''

\textcolor{label}{Version:} \tabto{8em} 1.9

\vfill

\AddToHook{shipout/background}{
    \begin{tikzpicture}[remember picture,overlay]
    \node[anchor=south east, inner sep=0] at (current page.south east) {
    \includegraphics[width=3.46in]{title-page-footer}
    };
    \end{tikzpicture}
}
\thispagestyle{titlepage}
\end{titlepage}
\RemoveFromHook{shipout/background}
\AddToHook{shipout/background}{
      \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=south west, align=left, inner sep=0] at (current page.south west) {
        \includegraphics[width=6.72in]{normal-page-footer}
      };
      \end{tikzpicture}
      \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=north east, opacity=0.5, inner sep=35] at (current page.north east) {
        \includegraphics[width=4cm]{normal-page-header}
      };
      \end{tikzpicture}
    }
''',
}