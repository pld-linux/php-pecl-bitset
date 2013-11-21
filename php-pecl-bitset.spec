%define		php_name	php%{?php_suffix}
%define		modname	bitset
Summary:	%{modname} - managing sets of bits
Summary(pl.UTF-8):	%{modname} - obróbka zbiorów bitów
Name:		%{php_name}-pecl-%{modname}
Version:	2.0
Release:	1
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	377e3e3ce071ac10908df8ccdd4a5a26
URL:		http://pecl.php.net/package/bitset/
BuildRequires:	%{php_name}-devel >= 3:5.3.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The BitSet library assists by providing a mechanism to manage sets of
bits. This provides a similar API (object-based) to java.util.BitSet
with some PHP-specific flavoring.

The original functions provided under 1.0 are still available, though
deprecated as of 2.0 and will be removed under 3.0.

IMPORTANT: Versions 2.0 and higher of this extension require PHP 5.3+

%description -l pl.UTF-8
Rozszerzenie to jest biblioteką do zarządzania zbiorami bitów w
rozumieniu Teorii Zbiorów.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
