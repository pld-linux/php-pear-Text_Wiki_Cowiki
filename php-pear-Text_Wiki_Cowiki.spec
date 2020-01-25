%define		_class		Text
%define		_subclass	Wiki_Cowiki
%define		_status		alpha
%define		_pearname	Text_Wiki_Cowiki
Summary:	%{_pearname} - Cowiki parser and renderer for Text_Wiki
Summary(pl.UTF-8):	%{_pearname} - analizator i renderer coWiki dla Text_Wiki
Name:		php-pear-%{_pearname}
Version:	0.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	131713e1f47e5938adf541139189243f
URL:		http://pear.php.net/package/Text_Wiki_Cowiki/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Text_Wiki >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Note: coWiki has been offically discontinued. This package is being
kept to allow conversion of coWiki syntax to other wiki markups.

Parses coWiki mark-up to tokenize the text for Text_Wiki rendering
and also renders for wiki conversion.

See: <http://cowiki.org/>
 
In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Uwaga: coWiki oficjalnie przestało być utrzymywane. Ten pakiet został
zachowany w celu konwersji ze składni coWiki do znaczników innych
wiki.

Ta klasa analizuje znaczniki coWiki w celu utworzenia tokenów tekstu
do renderowania Text_Wiki oraz konwersji wiki.

Więcej pod adresem <http://cowiki.org/>.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/Wiki/Cowiki.php
%{php_pear_dir}/Text/Wiki/Render/Cowiki.php
%{php_pear_dir}/Text/Wiki/Parse/Cowiki
%{php_pear_dir}/Text/Wiki/Render/Cowiki
