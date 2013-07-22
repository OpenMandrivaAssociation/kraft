Summary:	KDE software to manage office documents in the office
Name:		kraft
Version:	0.50
Release:	1
License:	GPLv2+
Group:		Office
Url:		http://volle-kraft-voraus.de
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:		kraft-0.50-cmake.patch
BuildRequires:	kdepimlibs4-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(libctemplate)
Requires:	python-pypdf
Requires:	python-reportlab
Requires:	sqlite3-tools

%description
Kraft is KDE software to help to create and manage office documents such
as offers and invoices in the small enterprise. It supports easy document
creation, templates with calculation, customer management through the KDE
addressbook, highly configurable PDF output and more.

See the website http://volle-kraft-voraus.de for more information.

%files -f %{name}.lang
%doc AUTHORS COPYING README Releasenotes.txt TODO
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}
%{_kde_appsdir}/kplant
%{_kde_datadir}/config.kcfg/databasesettings.kcfg
%{_kde_datadir}/config.kcfg/kraftsettings.kcfg
%{_kde_iconsdir}/*/*/*/%{name}*.png

#----------------------------------------------------------------------------

%define major 0
%define libkraftcat %mklibname kraftcat %{major}

%package -n %{libkraftcat}
Summary:	Shared library for Kraft
Group:		System/Libraries
Conflicts:	%{name} < 0.50

%description -n %{libkraftcat}
Shared library for Kraft.

%files -n %{libkraftcat}
%{_kde_libdir}/libkraftcat.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}
chmod 755 %{buildroot}%{_kde_appsdir}/%{name}/tools/erml2pdf.py

# We don't need this because there are no headers anyway
rm -f %{buildroot}%{_kde_libdir}/libkraftcat.so

