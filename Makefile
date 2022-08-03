PREFIX = /usr

all:
	@echo Run \'make install\' to install articblushifier.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p articblush.sh $(DESTDIR)$(PREFIX)/bin/articblushifier
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/articblushifier
	@cp -p conv.py $(DESTDIR)$(PREFIX)/bin/articblushifierpy
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/articblushifierpy


uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/articblushifier
	@rm -rf $(DESTDIR)$(PREFIX)/bin/articblushifierpy
