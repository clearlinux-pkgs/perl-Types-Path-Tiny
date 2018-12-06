#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Types-Path-Tiny
Version  : 0.006
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Types-Path-Tiny-0.006.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Types-Path-Tiny-0.006.tar.gz
Summary  : 'Path::Tiny types and coercions for Moose and Moo'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Types-Path-Tiny-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(File::pushd)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Type::Library)
BuildRequires : perl(Type::Utils)
BuildRequires : perl(Types::Standard)
BuildRequires : perl(Types::TypeTiny)

%description
NAME
Types::Path::Tiny - Path::Tiny types and coercions for Moose and Moo
VERSION
version 0.006

%package dev
Summary: dev components for the perl-Types-Path-Tiny package.
Group: Development
Provides: perl-Types-Path-Tiny-devel = %{version}-%{release}

%description dev
dev components for the perl-Types-Path-Tiny package.


%package license
Summary: license components for the perl-Types-Path-Tiny package.
Group: Default

%description license
license components for the perl-Types-Path-Tiny package.


%prep
%setup -q -n Types-Path-Tiny-0.006

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Types-Path-Tiny
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Types-Path-Tiny/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Types/Path/Tiny.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Types::Path::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Types-Path-Tiny/LICENSE
