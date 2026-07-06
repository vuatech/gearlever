%global debug_package %{nil}

Name:		gearlever
Version:	4.5.5
Release:	1
Source0:	https://github.com/mijorus/gearlever/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Manage AppImages with ease
URL:		https://github.com/mijorus/gearlever
License:	GPLv3
Group:		Package Management

#BuildSystem:	meson
BuildRequires:	meson
BuildRequires:	gettext
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	gtk-update-icon-cache
BuildRequires:	desktop-file-utils

Requires:	python%{pyver}dist(pygobject)
Requires:	python%{pyver}dist(pydbus)
Requires:	python%{pyver}dist(desktop-entry-lib)
Requires:       python%{pyver}dist(ftputil)

Requires:	%{mklibname adwaita}
Requires:   	python%{pyver}dist(pyxdg)

#Removed due to not being an hard dependency. 
#Requires:   	fcitx-gtk3

%description
%summary

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_install
sed -i '1s|^#!/bin/python3|#!/usr/bin/python3|' %{buildroot}%{_bindir}/gearlever

%files
%{_bindir}/%{name}
%{_datadir}/metainfo/it.mijorus.gearlever.metainfo.xml
%{_datadir}/%{name}
%{_iconsdir}/hicolor/scalable/actions/*
%{_datadir}/applications/*
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/gearlever.mo
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/gearlever.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/gearlever.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/gearlever.mo
%lang(fi_FI) %{_datadir}/locale/fi_FI/LC_MESSAGES/gearlever.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/gearlever.mo
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/gearlever.mo
%lang(hi) %{_datadir}/locale/hi/LC_MESSAGES/gearlever.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/gearlever.mo
%lang(ka) %{_datadir}/locale/ka/LC_MESSAGES/gearlever.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/gearlever.mo
%lang(oc) %{_datadir}/locale/oc/LC_MESSAGES/gearlever.mo
%lang(pl_PL) %{_datadir}/locale/pl_PL/LC_MESSAGES/gearlever.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/gearlever.mo
%lang(pt_PT) %{_datadir}/locale/pt_PT/LC_MESSAGES/gearlever.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/gearlever.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/gearlever.mo
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/gearlever.mo
%lang(vi) %{_datadir}/locale/vi/LC_MESSAGES/gearlever.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/gearlever.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/gearlever.mo
%{_iconsdir}/*/*/*/it.mijorus.gearlever*
%{_datadir}/glib-2.0/*/it.mijorus.gearlever.gschema.xml
