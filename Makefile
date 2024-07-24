# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
VENV          = .sphinx/venv/bin/activate
TEMPLATE      = NONE


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

install:
	@echo "... setting up virtualenv"
	python3 -m venv .sphinx/venv
	. $(VENV); pip install --upgrade -r .sphinx/requirements.txt

	@echo "\n" \
		"--------------------------------------------------------------- \n" \
		"* watch, build and serve the documentation: make run \n" \
                "* only build: make html \n" \
                "* only serve: make serve \n" \
                "* clean built doc files: make clean-doc \n" \
                "* clean full environment: make clean \n" \
		"* check spelling: make spelling \n" \
                "* check inclusive language: make woke \n" \
		"--------------------------------------------------------------- \n"
run:
	. $(VENV); export TEMPLATE=$(TEMPLATE) &&  sphinx-autobuild -c . -b dirhtml "$(SOURCEDIR)" "$(BUILDDIR)"

html:
	. $(VENV); export TEMPLATE=$(TEMPLATE) && $(SPHINXBUILD) -c . -b dirhtml "$(SOURCEDIR)" "$(BUILDDIR)" -w .sphinx/warnings.txt

epub:
	. $(VENV); $(SPHINXBUILD) -c . -b epub "$(SOURCEDIR)" "$(BUILDDIR)" -w .sphinx/warnings.txt

serve:
	cd "$(BUILDDIR)"; python3 -m http.server 8000

clean: clean-doc
	rm -rf .sphinx/venv

clean-doc:
	git clean -fx "$(BUILDDIR)"

spelling: html
	. $(VENV) ; python3 -m pyspelling -c .sphinx/spellingcheck.yaml

linkcheck:
	. $(VENV) ; $(SPHINXBUILD) -c . -b linkcheck  "$(SOURCEDIR)" "$(BUILDDIR)"

woke:
	type woke >/dev/null 2>&1 || { snap install woke; exit 1; }
	woke *.rst **/*.rst -c https://github.com/canonical-web-and-design/Inclusive-naming/raw/main/config.yml

pdf-prep: install
	@. $(VENV); (dpkg-query -W -f='$${Status}' latexmk 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package latexmk is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' fonts-freefont-otf 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package fonts-freefont-otf is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' fonts-ibm-plex 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package fonts-ibm-plex is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' texlive-latex-recommended 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package texlive-latex-recommended is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' texlive-latex-extra 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package texlive-latex-extra is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' texlive-fonts-recommended 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package texlive-fonts-recommended is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' texlive-font-utils 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package texlive-font-utils is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' texlive-lang-cjk 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package texlive-lang-cjk is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' texlive-xetex 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package texlive-xetex is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' plantuml 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package plantuml is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' xindy 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package xindy is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' tex-gyre 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package tex-gyre is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)
	@. $(VENV); (dpkg-query -W -f='$${Status}' dvipng 2>/dev/null | grep -c "ok installed" >/dev/null && echo "Package dvipng is installed") || (echo "PDF generation requires the installation of the following packages: latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng" && echo "" && echo "make pdf-prep-force will install these packages" && echo "" && echo "Please be aware these packages will be installed to your system" && false)

# Entrypoint to install system packages, separate from usual workflow due to permanence

pdf-prep-force:
	apt-get update
	apt-get install --no-install-recommends -y latexmk fonts-freefont-otf fonts-ibm-plex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-font-utils texlive-lang-cjk texlive-xetex plantuml xindy tex-gyre dvipng \

pdf: pdf-prep
	@. $(VENV); export TEMPLATE=$(TEMPLATE) && sphinx-build -M latexpdf "$(SOURCEDIR)" "_build" $(SPHINXOPTS)
	@. $(VENV); rm ./_build/latex/front-page-light.pdf || true
	@. $(VENV); rm ./_build/latex/normal-page-footer.pdf || true
	@. $(VENV); find ./_build/latex -name "*.pdf" -exec mv -t ./ {} +
	@. $(VENV); rm -r _build

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	. $(VENV); $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
