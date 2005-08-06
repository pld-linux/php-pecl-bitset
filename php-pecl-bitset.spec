%define		_modname	bitset
%define		_status		stable

Summary:	%{_modname} - managing sets of bits
Summary(pl):	%{_modname} - obróbka zbiorów bitów
Name:		php-pecl-%{_modname}
Version:	1.0
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	9a4514a398a1b192fe215521db5f7546
URL:		http://pecl.php.net/package/bitset/
BuildRequires:	libtool
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This extension is a library for managing sets of bits in terms of Set
Theory.

In PECL status of this extension is: %{_status}.

%description -l pl
Rozszerzenie to jest bibliotek± do zarz±dzania zbiorami bitów w
rozumieniu Teorii Zbiorów.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL,README}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
