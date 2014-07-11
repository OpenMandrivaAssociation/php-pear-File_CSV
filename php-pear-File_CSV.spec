%define	_class	File
%define	modname	%{_class}_CSV

Summary:	Read and write of CSV files
Name:		php-pear-%{modname}
Version:	1.0.0
Release:	11
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/File_CSV/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun): php-pear
Requires:	php-pear
Conflicts:	php-pear-File < 1.4.0

%description
Read and write of CSV files as well as discovering the format the CSV file is
in.

Supports headers and is excel compatible, i.e. ="0004" outputs as 0004 (only
read wise)

For more information on CSV: http://rfc.net/rfc4180.html

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}/CSV.php
%{_datadir}/pear/packages/%{modname}.xml

