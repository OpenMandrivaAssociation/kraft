%define beta rc1

Summary:	KDE software to manage office documents in the office
Name:		kraft
Version:	1.0
Release:	%{?beta:0.%{beta}.1}1
License:	GPLv2+
Group:		Office
Url:		http://volle-kraft-voraus.de
Source0:	https://github.com/dragotin/kraft/archive/v%{version}%{?beta:%{beta}}/%{name}-%{version}%{?beta:%{beta}}.tar.gz
BuildRequires:	pkgconfig(libctemplate)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Grantlee5)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	gettext-devel
BuildRequires:	asciidoctor
BuildRequires:	po4a
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
%doc AUTHORS COPYING Releasenotes.txt TODO
%{_bindir}/%{name}
%{_bindir}/findcontact
%{_datadir}/applications/de.volle_kraft_voraus.%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/config.kcfg/databasesettings.kcfg
%{_datadir}/config.kcfg/kraftsettings.kcfg
%{_datadir}/icons/*/*/*/%{name}*.*
%{_datadir}/kxmlgui5/kraft
%{_datadir}/metainfo/de.volle_kraft_voraus.kraft.appdata.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:%{beta}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name}
