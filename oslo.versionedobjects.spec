#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.versionedobjects
Version  : 0.10.0
Release  : 6
URL      : http://tarballs.openstack.org/oslo.versionedobjects/oslo.versionedobjects-0.10.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.versionedobjects/oslo.versionedobjects-0.10.0.tar.gz
Summary  : Oslo Versioned Objects library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.versionedobjects-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Paste-python
BuildRequires : PasteDeploy-python
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Routes-python
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : aioeventlet-python
BuildRequires : amqp-python
BuildRequires : anyjson-python
BuildRequires : cachetools-python
BuildRequires : contextlib2-python
BuildRequires : debtcollector-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fasteners-python
BuildRequires : fixtures-python
BuildRequires : funcsigs-python
BuildRequires : futures-python
BuildRequires : futurist-python
BuildRequires : greenlet-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : kombu-python
BuildRequires : linecache2-python
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : os-client-config-python
BuildRequires : oslo.concurrency-python
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslo.messaging-python
BuildRequires : oslo.middleware-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.service-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : posix_ipc
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : repoze.lru-python
BuildRequires : requests-python
BuildRequires : retrying-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : trollius-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
===================================
oslo.versionedobjects
===================================

%package python
Summary: python components for the oslo.versionedobjects package.
Group: Default

%description python
python components for the oslo.versionedobjects package.


%prep
%setup -q -n oslo.versionedobjects-0.10.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
