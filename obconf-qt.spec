%define		qtver		4.8.5

Summary:	obconf-qt
Name:		obconf-qt
Version:	0.1.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/obconf-qt/0.1.0/%{name}-%{version}.tar.xz
# Source0-md5:	d08c292eae465b21a1635d1b4b5372d6
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
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
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
%{_pixmapsdir}/obconf-qt.png
