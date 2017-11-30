#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-polib
Version  : 1.1.0
Release  : 3
URL      : https://pypi.io/packages/source/p/polib/polib-1.1.0.tar.gz
Source0  : https://pypi.io/packages/source/p/polib/polib-1.1.0.tar.gz
Summary  : A library to manipulate gettext files (po and mo files).
Group    : Development/Tools
License  : MIT
Requires: python-polib-legacypython
Requires: python-polib-python3
Requires: python-polib-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=====
        polib
        =====

%package legacypython
Summary: legacypython components for the python-polib package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the python-polib package.


%package python
Summary: python components for the python-polib package.
Group: Default
Requires: python-polib-legacypython
Requires: python-polib-python3

%description python
python components for the python-polib package.


%package python3
Summary: python3 components for the python-polib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-polib package.


%prep
%setup -q -n polib-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512065333
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1512065333
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
