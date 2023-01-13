Name:           jbigkit
Version:        2.1
Release:        20
Summary:        Lossless image compression library

License:        GPLv2+
URL:            https://www.cl.cam.ac.uk/~mgk25/jbigkit/
Source0:        https://www.cl.cam.ac.uk/~mgk25/jbigkit/download/%{name}-%{version}.tar.gz

# these patches come from fedora
Patch0:         jbigkit-2.1-shlib.patch
Patch1:         jbigkit-2.0-warnings.patch
Patch2:         jbigkit-ldflags.patch
Patch6000:      backport-CVE-2017-9937.patch

BuildRequires:  gcc vim
Requires:       %{name}-libs = %{version}-%{release}

%description
JBIG-KIT provides a portable library of compression and decompression
functions with a documented interface that you can include very easily
into your image or document processing software. In addition, JBIG-KIT
provides ready-to-use compression and decompression programs with a
simple command line interface.

%package        libs
Summary:        Libraries for %{name}

%description    libs
Libraries for %{name}.

%package        devel
Summary:        Files for %{name} development
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
files for %{name} development.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
export CFLAGS="${CFLAGS:-%optflags}" 
export CXXFLAGS="${CXXFLAGS:-%optflags}" 
export FFLAGS="${FFLAGS:-%optflags}"
make

%install
pushd libjbig
install -Dm 0644 -t %{buildroot}%{_includedir} *.h
install -Dm 0755 -t %{buildroot}%{_libdir} *.so*
popd
ln -sf libjbig.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libjbig.so
ln -sf libjbig85.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libjbig85.so
pushd pbmtools
install -Dm 0755 -t %{buildroot}%{_bindir} ???to??? ???to???85
install -Dm 0644 -t %{buildroot}%{_mandir}/man1/ *.1
popd

%check
make test

%ldconfig_scriptlets libs

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/*

%files libs
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so

%files help
%defattr(-,root,root)
%doc ANNOUNCE CHANGES TODO
%{_mandir}/man1/*

%changelog
* Fri Jan 13 2023 zhouwenpei <zhouwenpei1@h-partners.com> - 2.1-20
- fix build fail

* Tue Feb 9 2021 jinzhimin <jinzhimin2@huawei.com> - 2.1-19
- fix CVE-2017-9937

* Tue Feb 9 2021 jinzhimin <jinzhimin2@huawei.com> - 2.1-18
- add CFLAGS in build

* Mon Feb 17 2020 hexiujun <hexiujun1@huawei.com> - 2.1-17
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:unpack libs subpackage

* Thu Sep 5 2019 openEuler Builteam <buildteam@openeuler.org> - 2.1-16
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add requires

* Tue Aug 20 2019 openEuler Builteam <buildteam@openeuler.org> -2.1-15
- Package init
