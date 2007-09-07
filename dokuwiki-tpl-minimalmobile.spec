%define		_tpl		minimalmobile
Summary:	Minimal Mobile template for DokuWiki
Name:		dokuwiki-tpl-%{_tpl}
Version:	0
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://www.commitment.es/minimalmobile/minimalmobile.zip
# Source0-md5:	4be0786c41b63d9988e51aa51d659670
URL:		http://wiki.splitbrain.org/wiki:tpl:minimal_mobile
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_tpldir		%{_dokudir}/lib/tpl/%{_tpl}

%description
A very minimal template, with almost no margins, modified from the default
template. The image displays a "narrow browser", equivalent to what a user can
see in a mobile (albeit with lots of scrolling).

Features:
- Moved top bar and breadcrumbs to bottom
- Made most things small, and removed most padding and extra stuff
- Still fully functional
- Not pretty on big screen, but usable.

%prep
%setup -qc

cat > INSTALL <<'EOF'
To activate this template add the following to your conf/local.php file: 
$conf['template']    = '%{_tpl}';

Get rid of the TOC, that takes a lot of space in mobile screens.
$conf['toptoclevel'] = 0;  // Level starting with and below to include in AutoTOC (max. 5)
$conf['maxtoclevel'] = 0;  // Up to which level include into AutoTOC (max. 5)
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_tpldir}
cp -a minimalmobile/* $RPM_BUILD_ROOT%{_tpldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL
%{_tpldir}
