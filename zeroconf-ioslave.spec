Name:		zeroconf-ioslave
Summary:	DNS-SD Service Discovery Monitor
Group:		Networking/Other
Version:	16.08.2
Release:	1
URL:		http://www.kde.org
License:	GPLv2 LGPLv2 GFDL
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
Requires:	nss_mdns
Conflicts:	kdenetwork4-devel < 3:4.6.95

%description
DNS-SD Service Discovery Monitor.

%files
%dir %_kde_appsdir/remoteview
%_kde_appsdir/remoteview/zeroconf.desktop
%_kde_libdir/kde4/kded_dnssdwatcher.so
%_kde_libdir/kde4/kio_zeroconf.so
%_kde_services/kded/dnssdwatcher.desktop
%_kde_services/zeroconf.protocol
%_datadir/dbus-1/interfaces/org.kde.kdnssd.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
export LD=/usr/bin/ld.gold
%cmake_kde4 -DKDE4_ENABLE_FINAL=ON -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

