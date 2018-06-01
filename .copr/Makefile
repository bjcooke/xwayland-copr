DNF=/usr/bin/dnf
RPMBUILD=/usr/bin/rpmbuild


srpm:	xorg-x11-server-Xwayland-srpm

rpm-build:
	$(DNF) -y install $@

xorg-x11-server-Xwayland-srpm:	rpm-build
	$(RPMBUILD) -bs \
		--define="_topdir `pwd`" \
		--define="_sourcedir `pwd`" \
		--define="_specdir `pwd`" \
		--define="_srcrpmdir $(outdir)" \
		$(spec)
