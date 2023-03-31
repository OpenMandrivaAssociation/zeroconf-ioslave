%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

# We're keeping the original name until Plasma 6
# No need to mess with Provides: and Obsoletes:
# for a few months...
Name:		zeroconf-ioslave
Summary:	DNS-SD Service Discovery Monitor
Group:		Networking/Other
Version:	22.12.3
Release:	2
URL:		http://www.kde.org
License:	GPLv2 LGPLv2 GFDL
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kio-zeroconf-%{version}.tar.xz
Requires:	nss_mdns
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF5CoreAddons) cmake(KF5DBusAddons) cmake(KF5DNSSD) cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO) cmake(Qt5Core) cmake(Qt5DBus)

%description
DNS-SD Service Discovery Monitor.

%files -f %{name}.lang
%{_datadir}/remoteview
%{_libdir}/qt5/plugins/kf5/kded/dnssdwatcher.so
%{_libdir}/qt5/plugins/kf5/kio/zeroconf.so
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
%{_datadir}/metainfo/org.kde.kio_zeroconf.metainfo.xml

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kio-zeroconf-%{version}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
