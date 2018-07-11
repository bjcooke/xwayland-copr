Name:           xorg-x11-server-Xwayland
Version:        1.20.0
Release:        2%{?dist}
Summary:        Wayland X Server

License:        MIT
URL:            https://www.x.org
Source0:        https://www.x.org/archive/individual/xserver/xorg-server-%{version}.tar.bz2
Source1:        Xwayland.sh

BuildRequires: pkgconfig
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: pkgconfig(wayland-client) >= 1.3.0
BuildRequires: egl-wayland-devel >= 1.0.3
BuildRequires: pkgconfig(epoxy) >= 1.5.2
%if 0%{?fedora} > 24  || 0%{?rhel} > 7
BuildRequires: pkgconfig(xshmfence) >= 1.1
%endif
BuildRequires: systemtap-sdt-devel
BuildRequires: libXv-devel
BuildRequires: pixman-devel >= 0.30.0
BuildRequires: libpciaccess-devel >= 0.13.1 openssl-devel bison flex flex-devel
BuildRequires: mesa-libGL-devel >= 9.2
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: libdrm-devel >= 2.4.0 kernel-headers
BuildRequires: xorg-x11-util-macros >= 1.17
BuildRequires: xorg-x11-proto-devel >= 7.7.1.20
BuildRequires: xorg-x11-font-utils >= 7.2-11
BuildRequires: dbus-devel libepoxy-devel systemd-devel
BuildRequires: xorg-x11-xtrans-devel >= 1.3.2
BuildRequires: libXfont2-devel libXau-devel libxkbfile-devel libXres-devel
BuildRequires: libfontenc-devel libXtst-devel libXdmcp-devel
BuildRequires: libX11-devel libXext-devel
BuildRequires: libXinerama-devel libXi-devel
BuildRequires: libdrm-devel >= 2.4.0 kernel-headers
BuildRequires: audit-libs-devel libselinux-devel >= 2.0.86-1
BuildRequires: libudev-devel
%if 0%{?fedora} > 24  || 0%{?rhel} > 7
# libunwind is Exclusive for the following arches
%ifarch aarch64 %{arm} hppa ia64 mips ppc ppc64 %{ix86} x86_64
BuildRequires: libunwind-devel
%endif
%endif
BuildRequires: pkgconfig(xcb-aux) pkgconfig(xcb-image) pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms) pkgconfig(xcb-renderutil)


Requires: xorg-x11-server-common

%description
Xwayland is an X server for running X clients under Wayland.


%prep
%autosetup -n xorg-server-%{version}


%build
%configure \
	--disable-docs \
	--disable-devel-docs \
	--disable-xorg \
	--disable-xvfb \
	--disable-xnest \
	--enable-xwayland \
	--enable-xwayland-eglstream \
	--enable-glx \
	--enable-config-udev \
	--enable-config-udev-kms


%make_build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{_builddir}/xorg-server-%{version}/hw/xwayland/Xwayland $RPM_BUILD_ROOT%{_libexecdir}/Xwayland
install -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/Xwayland

%files
%{_libexecdir}/Xwayland
%{_bindir}/Xwayland
%license COPYING



%changelog
* Mon Jul 10 2018 Benjamin Cooke <bcooke@freedomofknowledge.org> - 1.20.0-2
- Add egl-wayland-devel build dependency

* Fri Jun  1 2018 Benjamin Cooke <bcooke1@umbc.edu>
- First goatrope
