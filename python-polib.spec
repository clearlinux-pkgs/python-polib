#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-polib
Version  : 1.1.1
Release  : 33
URL      : https://files.pythonhosted.org/packages/de/37/88ad2639cb4396755e87e97229d268bfa8bae0aeb6c7f9b01e9f49e10dff/polib-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/37/88ad2639cb4396755e87e97229d268bfa8bae0aeb6c7f9b01e9f49e10dff/polib-1.1.1.tar.gz
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
        
        |build-status-image| |codecov-image| |documentation-status-image| |pypi-version| |py-versions|
        
        Overview
        --------
        
        polib is a library to manipulate, create, modify gettext files (pot, po and mo
        files). You can load existing files, iterate through it's entries, add, modify
        entries, comments or metadata, etc... or create new po files from scratch.
        
        polib supports out of the box any version of python ranging from 2.7 to latest
        3.X version.
        
        polib is pretty stable now and is used by many

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
%setup -q -n polib-1.1.1
cd %{_builddir}/polib-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617057866
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
mkdir -p %{buildroot}/usr/share/package-licenses/python-polib
cp %{_builddir}/polib-1.1.1/LICENSE %{buildroot}/usr/share/package-licenses/python-polib/9839a383fb7673f28658945f03d4a127980cdda2
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
