Name:           kraft
Url:            http://volle-kraft-voraus.de
Version:        0.45
Release:        1
License:        GPL, LGPL
Summary:        KDE software to manage office documents in the office
Group:          Office
Source0:        kraft-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE kraft-%{version}.dif freitag@opensuse.org -- fix cmake input file
Patch0:         kraft-%{version}.dif
Patch1:         kraft_follower.dif

Requires:       python-pypdf
Requires:       python-reportlab
Requires:       sqlite3

BuildRequires:  libctemplate-devel
BuildRequires:  qt4-devel
BuildRequires:  kdepimlibs4-devel

%description
Kraft is KDE software to help to
create and manage office documents such as
offers and invoices in the small enterprise.

It supports easy document creation,
templates with calculation, customer management
through the KDE addressbook, highly
configurable PDF output and more.

See the website http://volle-kraft-voraus.de
for more information.

%prep
%setup -q
%patch0
%patch1

%build
%cmake_kde4
%make

%install
cd build
%makeinstall_std
cd ..
%find_lang %{name}
chmod 755 %{buildroot}%{_datadir}/apps/kraft/tools/erml2pdf.py

%files -f %{name}.lang
%{_bindir}/kraft
%{_bindir}/kplant
%{_libdir}/libkraftcat*
%{_datadir}/applications/kde4/kraft.desktop
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/apps/%{name}/
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/apps/kplant/pics/*.png

%doc AUTHORS COPYING INSTALL README Releasenotes.txt TODO
