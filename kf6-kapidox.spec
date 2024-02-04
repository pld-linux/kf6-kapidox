#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# - runtime Requires if any
# - python3 version
# - .pyo etc
%define		kdeframever	5.249.0
%define		qtver		5.15.2
%define		kfname		kapidox
Summary:	Kapidox
Name:		kf6-%{kfname}
Version:	5.249.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	d08881f3d846bec71d5ef003105e08aa
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.2.0
BuildRequires:	Qt6DBus-devel >= 5.2.0
BuildRequires:	Qt6Gui-devel >= 5.3.1
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel >= 5.2.0
BuildRequires:	cmake >= 3.16
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	graphviz
Requires:	kf6-dirs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
This framework contains scripts and data for building API
documentation (dox) in a standard format and style.

The Doxygen tool is used to do the actual documentation extraction and
formatting, but this framework provides a wrapper script to make
generating the documentation more convenient (including reading
settings from the target framework or other module) and a standard
template for the generated documentation.

%prep
%setup -q -n %{kfname}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/depdiagram_generate_all
%attr(755,root,root) %{_bindir}/kapidox-depdiagram-generate
%attr(755,root,root) %{_bindir}/kapidox-depdiagram-prepare
%attr(755,root,root) %{_bindir}/kapidox-generate
%{py3_sitescriptdir}/kapidox/
%{py3_sitescriptdir}/kapidox-*.egg-info