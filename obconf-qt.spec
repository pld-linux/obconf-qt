%define		qtver		4.8.5

Summary:	obconf-qt
Name:		obconf-qt
Version:	0.11.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/obconf-qt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	12de451f5ab442bf6174ea285f2670e9
URL:		http://www.lxqt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	glib2-devel
BuildRequires:	openbox-devel >= 3.5
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obconf-qt

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/obconf-qt
%{_desktopdir}/obconf-qt.desktop
%{_iconsdir}/hicolor/48x48/apps/obconf-qt.png
