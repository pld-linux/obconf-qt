%define		qtver		6.6.0

Summary:	Qt port of a configuration editor for OpenBox window manager
Summary(pl.UTF-8):	Port Qt edytora konfiguracji dla menedżera okien OpenBox
Name:		obconf-qt
Version:	0.16.6
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	https://github.com/lxqt/obconf-qt/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	24eb56d0aac8099cbceeff412d82c4c9
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.5.0
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	lxqt-build-tools >= 2.3.0
BuildRequires:	openbox-devel >= 1:3.5
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObConf-Qt is a Qt port of ObConf, a configuration editor for window
manager OpenBox.

It is not actively developed anymore by LXQt project, code
contributions and bugfixes will be accepted. It can be used
independently from this desktop environment.

%description -l pl.UTF-8
ObConf-Qt to port Qt programu ObConf, edytora konfiguracji dla
menedżera okien OpenBox.

Nie jest on już aktywnie rozwijany przez projekt LXQt, akceptowany
jest wkład w postaci kodu i poprawek błędów. Można go używać
niezależnie od tego środowiska graficznego.

%prep
%setup -q

%build
%cmake -B build \
	-DPULL_TRANSLATIONS:BOOL=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/obconf-qt
%{_desktopdir}/obconf-qt.desktop
%{_iconsdir}/hicolor/48x48/apps/obconf-qt.png
