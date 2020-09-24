#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-polib
Version  : 1.1.0
Release  : 22
URL      : https://pypi.io/packages/source/p/polib/polib-1.1.0.tar.gz
Source0  : https://pypi.io/packages/source/p/polib/polib-1.1.0.tar.gz
Summary  : A library to manipulate gettext files (po and mo files).
Group    : Development/Tools
License  : MIT
Requires: python-polib-license = %{version}-%{release}
Requires: python-polib-python = %{version}-%{release}
Requires: python-polib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=====
        polib
        =====

%package license
Summary: license components for the python-polib package.
Group: Default

%description license
license components for the python-polib package.


%package python
Summary: python components for the python-polib package.
Group: Default
Requires: python-polib-python3 = %{version}-%{release}

%description python
python components for the python-polib package.


%package python3
Summary: python3 components for the python-polib package.
Group: Default
Requires: python3-core
Provides: pypi(polib)

%description python3
python3 components for the python-polib package.


%prep
%setup -q -n polib-1.1.0
cd %{_builddir}/polib-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583697592
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-polib
cp %{_builddir}/polib-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/python-polib/9839a383fb7673f28658945f03d4a127980cdda2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-polib/9839a383fb7673f28658945f03d4a127980cdda2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
