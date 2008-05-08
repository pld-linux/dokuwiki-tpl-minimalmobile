%define		tpl	minimalmobile
Summary:	Minimal Mobile template for DokuWiki
Summary(pl.UTF-8):	Szablon Minimal Mobile dla DokuWiki
Name:		dokuwiki-tpl-%{tpl}
Version:	20070712
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://www.commitment.es/minimalmobile/minimalmobile.zip
# Source0-md5:	4be0786c41b63d9988e51aa51d659670
URL:		http://wiki.splitbrain.org/wiki:tpl:minimal_mobile
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		tpldir		%{dokudir}/lib/tpl/%{tpl}

%description
A very minimal template, with almost no margins, modified from the
default template. The image displays a "narrow browser", equivalent
to what a user can see in a mobile (albeit with lots of scrolling).

Features:
- Moved top bar and breadcrumbs to bottom
- Made most things small, and removed most padding and extra stuff
- Still fully functional
- Not pretty on big screen, but usable.

%description -l pl.UTF-8
Naprawdę minimalistyczny szablon, prawie bez marginesów, przerobiony
z szablonu domyślnego. Wyświetla "wąską przeglądarkę", odpowiadającą
temu, co użytkownik może zobaczyć w telefonie (tyle że z dużą ilością
przewijania).

Cechy szablonu:
- ma górny pasek i przyciski nawigacyjne przeniesione na dół
- jest wykonany ze zmniejszoną większością elementów i usuniętą
  większością odstępów oraz elementów dodatkowych
- jest nadal w pełni funkcjonalny
- nie wygląda najpiękniej na dużym ekranie, ale jest używalny.

%prep
%setup -qc

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file:
$conf['template']    = '%{tpl}';

Get rid of the TOC, that takes a lot of space in mobile screens.
$conf['toptoclevel'] = 0;  // Level starting with and below to include in AutoTOC (max. 5)
$conf['maxtoclevel'] = 0;  // Up to which level include into AutoTOC (max. 5)
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tpldir}
cp -a minimalmobile/* $RPM_BUILD_ROOT%{tpldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL
%{tpldir}
