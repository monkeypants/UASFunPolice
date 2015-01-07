
.PHONY: generate_docs apidoc docs clean_generated_docs

docs: apidoc clean_generated_docs generate_docs
	@echo "# making docs"
	make html; make latexpdf > latex.log 2> latex_err.log;

generate_docs:
	mkdir _generated
	mkdir _generated/actors
	mkdir _generated/features
	mkdir _generated/glossary
	python dsl/behavior.py --rst=_generated

clean_generated_docs:
	rm -rf _generated/

apidoc:
	@echo "# auto-generating docs"
	rm -rf api/*
	sphinx-apidoc -o api ./
	echo "docs/api/ is purely generated content, do not edit." > api/README
	rm api/modules.rst; rm api/conf.rst  # that file is redundant
	
