# $Id$

# Authority: dag
# Upstream: <xfrisk-devel$tuxick,net>

%{?dist: %{expand: %%define %dist 1}}

Summary: Multi-user network version of the classic "Risk"
Name: xfrisk
Version: 1.2
Release: 0
License: GPL
Group: Amusements/Games
URL: http://tuxick.net/xfrisk/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://tuxick.net/xfrisk/files/XFrisk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?dist:BuildRequires: xorg-x11-devel}
%{?fc2:BuildRequires: xorg-x11-devel}
%{?fc1:BuildRequires: XFree86-devel}
%{?rh9:BuildRequires: XFree86-devel}

Obsoletes: XFrisk

%description
XFrisk is a computer version of the classic Risk board game. It is
a multiplayer game played on a TCP/IP network, uses the X11 window
system for graphics and runs on most UNIX and UNIX-like platforms.

%prep
%setup -n XFrisk

%build
%{__make} %{?_smp_mflags} \
	PREFIX="%{_prefix}" \
	BINDIR="%{_bindir}" \
	LIBDIR="%{_libdir}/xfrisk"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	LIBDIR="%{buildroot}%{_libdir}/xfrisk"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING FAQ README.NEW TODO
%{_bindir}/*
%{_libdir}/xfrisk/

%changelog
#- Updated URL and Source-tag. (Anthony Joseph Seward)

* Sat Feb 15 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package. (using DAR)
