#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : oslo.versionedobjects
Version  : 2.3.0
Release  : 58
URL      : http://tarballs.openstack.org/oslo.versionedobjects/oslo.versionedobjects-2.3.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.versionedobjects/oslo.versionedobjects-2.3.0.tar.gz
Source1  : http://tarballs.openstack.org/oslo.versionedobjects/oslo.versionedobjects-2.3.0.tar.gz.asc
Summary  : Oslo Versioned Objects library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.versionedobjects-license = %{version}-%{release}
Requires: oslo.versionedobjects-python = %{version}-%{release}
Requires: oslo.versionedobjects-python3 = %{version}-%{release}
Requires: WebOb
Requires: iso8601
Requires: netaddr
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.serialization
Requires: oslo.utils
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : iso8601
BuildRequires : netaddr
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package license
Summary: license components for the oslo.versionedobjects package.
Group: Default

%description license
license components for the oslo.versionedobjects package.


%package python
Summary: python components for the oslo.versionedobjects package.
Group: Default
Requires: oslo.versionedobjects-python3 = %{version}-%{release}

%description python
python components for the oslo.versionedobjects package.


%package python3
Summary: python3 components for the oslo.versionedobjects package.
Group: Default
Requires: python3-core
Provides: pypi(oslo.versionedobjects)
Requires: pypi(iso8601)
Requires: pypi(netaddr)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.context)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.messaging)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.utils)
Requires: pypi(webob)

%description python3
python3 components for the oslo.versionedobjects package.


%prep
%setup -q -n oslo.versionedobjects-2.3.0
cd %{_builddir}/oslo.versionedobjects-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600110068
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.versionedobjects
cp %{_builddir}/oslo.versionedobjects-2.3.0/LICENSE %{buildroot}/usr/share/package-licenses/oslo.versionedobjects/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.versionedobjects/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
