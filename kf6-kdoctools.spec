%define libname %mklibname KF6DocTools
%define devname %mklibname KF6DocTools -d
%define git 20231005

Name: kf6-kdoctools
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kdoctools/-/archive/master/kdoctools-master.tar.bz2#/kdoctools-%{git}.tar.bz2
Summary: Create documentation from DocBook
URL: https://invent.kde.org/frameworks/kdoctools
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6I18n)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: libxml2-utils
BuildRequires: docbook-dtds
BuildRequires: perl(URI::Escape)
Requires: %{libname} = %{EVRD}
Requires: docbook-dtd45-xml
Requires: docbook-style-xsl

%description
Create documentation from DocBook

%package -n %{libname}
Summary: Create documentation from DocBook
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Create documentation from DocBook

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Create documentation from DocBook

%prep
%autosetup -p1 -n kdoctools-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html --with-man

%files -f %{name}.lang
%{_bindir}/checkXML6
%{_bindir}/meinproc6
%{_datadir}/kf6/kdoctools
%{_mandir}/man1/checkXML6.1*
%{_mandir}/man1/meinproc6.1*
%{_mandir}/man7/kf6options.7*
%{_mandir}/man7/qt6options.7*

%files -n %{devname}
%{_includedir}/KF6/KDocTools
%{_libdir}/cmake/KF6DocTools
%{_qtdir}/doc/KF6DocTools.*

%files -n %{libname}
%{_libdir}/libKF6DocTools.so*
