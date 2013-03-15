%define		_class		File
%define		upstream_name	%{_class}_CSV

Summary:	Read and write of CSV files
Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	5
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/File_CSV/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
Conflicts:	php-pear-File < 1.4.0

%description
Read and write of CSV files as well as discovering the format the CSV file is
in.

Supports headers and is excel compatible, i.e. ="0004" outputs as 0004 (only
read wise)

For more information on CSV: http://rfc.net/rfc4180.html

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}/CSV.php
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2011.0
+ Revision: 667496
- mass rebuild

* Tue Apr 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1
+ Revision: 650597
- import php-pear-File_CSV


* Tue Apr 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2010.2
- initial Mandriva package
