Name: drv-img
Version: 0.1.0
Release: 1 
Summary: A cli tool to inject diver and package to Linux iso image
License: GPLv2

URL:     https://github.com/IZUMI-Zu/%{name}
Source0: https://github.com/IZUMI-Zu/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-setuptools python3-devel
Requires: createrepo_c genisoimage isomd5sum kmod
Requires: python3-packaging python3-rpm python3-kickstart rpm coreutils squashfs-tools util-linux

%description
A cli tool to inject diver and package to Linux iso image

%prep
%autosetup -n %{name}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/%{name}
%doc README.md

%changelog
* Sun Sep 17 2023 binshuozu binshuozu@gmail.com - 0.1.0-1
- Initial package

