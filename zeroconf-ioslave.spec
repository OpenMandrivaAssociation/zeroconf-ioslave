#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#

%define rel 1

Name:    zeroconf-ioslave
Summary: DNS-SD Service Discovery Monitor
Group:   Networking/Other
Version: 15.08.1
Release:        %mkrel %{rel}
URL:            http://www.kde.org
License:        GPLv2 LGPLv2 GFDL
Source0:        http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires:  kdelibs4-devel

Requires:  nss_mdns
Conflicts: kdenetwork4-devel < 3:4.6.95
Conflicts: kdnssd < 3:4.12.95
Obsoletes: kdnssd < 3:4.12.95

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
%cmake_kde4 -DKDE4_ENABLE_FINAL=ON
%make

%install
%makeinstall_std -C build


%changelog
* Fri Sep 18 2015 neoclust <neoclust> 15.08.1-1.mga6
+ Revision: 880938
- New version 15.08.1

* Thu Aug 20 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 866381
- New version 15.08.0

* Thu Jul 30 2015 lmenut <lmenut> 15.07.80-1.mga6
+ Revision: 859205
- Update to KDE Applications 15.08 Beta

* Wed Dec 03 2014 lmenut <lmenut> 4.14.3-1.mga5
+ Revision: 800698
- Update to KDE SC 4.14.3

* Sat Oct 18 2014 lmenut <lmenut> 4.14.2-1.mga5
+ Revision: 787796
- Update to KDE SC 4.14.2

* Wed Oct 15 2014 umeabot <umeabot> 4.14.1-2.mga5
+ Revision: 739163
- Second Mageia 5 Mass Rebuild

* Thu Oct 02 2014 lmenut <lmenut> 4.14.1-1.mga5
+ Revision: 734650
- Update to KDE SC 4.14.1

* Tue Sep 16 2014 umeabot <umeabot> 4.14.0-2.mga5
+ Revision: 690868
- Mageia 5 Mass Rebuild

* Mon Aug 25 2014 lmenut <lmenut> 4.14.0-1.mga5
+ Revision: 667584
- Update to KDE SC 4.14.0
- Use official URL http://download.kde.org for Source

* Fri Aug 15 2014 lmenut <lmenut> 4.13.97-1.mga5
+ Revision: 663096
- Update to KDE SC 4.13.97 aka KDE SC 4.14 RC

* Sat Jul 26 2014 lmenut <lmenut> 4.13.95-1.mga5
+ Revision: 656774
- Update to KDE SC 4.13.95 aka KDE SC 4.14 Beta3

* Sat Jul 19 2014 lmenut <lmenut> 4.13.90-1.mga5
+ Revision: 653959
- Update to KDE SC 4.13.90 aka KDE SC 4.14 Beta2

* Mon Jul 14 2014 lmenut <lmenut> 4.13.80-1.mga5
+ Revision: 652070
- Update to KDE SC 4.13.80 aka KDE SC 4.14 Beta1

* Sun Jun 15 2014 lmenut <lmenut> 4.13.2-1.mga5
+ Revision: 636833
- Update to KDE SC 4.13.2

* Sat May 24 2014 lmenut <lmenut> 4.13.1-1.mga5
+ Revision: 625600
- Update to KDE SC 4.13.1

* Thu Apr 17 2014 lmenut <lmenut> 4.13.0-1.mga5
+ Revision: 615681
- Update to KDE SC 4.13.0

* Sat Mar 29 2014 lmenut <lmenut> 4.12.97-1.mga5
+ Revision: 609493
- Update to KDE SC 4.12.97 aka KDE SC 4.13 RC

* Sun Mar 23 2014 lmenut <lmenut> 4.12.95-1.mga5
+ Revision: 606934
- Update to KDE SC 4.12.95 aka KDE SC 4.13 Beta3
- rename kdnssd to zeroconf-ioslave as upstream

* Fri Mar 14 2014 neoclust <neoclust> 3:4.12.90-1.mga5
+ Revision: 603336
- New version 4.12.80

* Fri Mar 07 2014 neoclust <neoclust> 3:4.12.80-1.mga5
+ Revision: 600672
- New version 4.12.80
- New version 4.12.3
- New version 4.12.3

* Thu Feb 13 2014 neoclust <neoclust> 3:4.12.2-1.mga5
+ Revision: 590458
- New version 4.12.2

* Tue Feb 11 2014 neoclust <neoclust> 3:4.11.5-1.mga5
+ Revision: 589250
- New version 4.11.5

* Wed Dec 04 2013 lmenut <lmenut> 3:4.11.4-1.mga4
+ Revision: 554989
- Update tarball to KDE SC 4.11.4

* Thu Nov 14 2013 lmenut <lmenut> 3:4.11.3-1.mga4
+ Revision: 551257
- Update tarball to KDE SC 4.11.3

* Mon Oct 21 2013 umeabot <umeabot> 3:4.11.2-2.mga4
+ Revision: 540450
- Mageia 4 Mass Rebuild

* Thu Oct 03 2013 mikala <mikala> 3:4.11.2-1.mga4
+ Revision: 490839
- Update tarball to KDE SC 4.11.2

* Mon Sep 09 2013 mikala <mikala> 3:4.11.1-1.mga4
+ Revision: 476916
- Update tarball to KDE SC 4.11.1

* Sat Aug 10 2013 mikala <mikala> 3:4.11.0-1.mga4
+ Revision: 465313
- Update tarball to KDE SC 4.11.0
- Update tarball to KDE SC 4.11.0

* Sat Jul 27 2013 lmenut <lmenut> 3:4.10.97-1.mga4
+ Revision: 458903
- Update tarball to KDE SC 4.10.97 aka KDE SC 4.11 RC2

* Wed Jul 17 2013 lmenut <lmenut> 3:4.10.95-1.mga4
+ Revision: 455293
- Update tarball to KDE SC 4.10.95 aka KDE SC 4.11 RC1

* Fri Jun 28 2013 mikala <mikala> 3:4.10.90-1.mga4
+ Revision: 448030
- Update tarball to KDE SC 4.10.90 aka KDE SC 4.11 Beta 2
- imported package kdnssd

