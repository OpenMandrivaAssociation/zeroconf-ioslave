%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		zeroconf-ioslave
Summary:	DNS-SD Service Discovery Monitor
Group:		Networking/Other
Version:	19.04.1
Release:	1
URL:		http://www.kde.org
License:	GPLv2 LGPLv2 GFDL
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Requires:	nss_mdns
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF5CoreAddons) cmake(KF5DBusAddons) cmake(KF5DNSSD) cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO) cmake(Qt5Core) cmake(Qt5DBus)

%description
DNS-SD Service Discovery Monitor.

%files -f %{name}.lang
%{_datadir}/remoteview
%{_libdir}/qt5/plugins/kded_dnssdwatcher.so
%{_libdir}/qt5/plugins/kf5/kio/zeroconf.so
%{_datadir}/kservices5/kded/dnssdwatcher.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
