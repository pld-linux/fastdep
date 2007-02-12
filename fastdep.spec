Summary:	A fast dependency generator for C/C++ files
Summary(pl.UTF-8):	Szybki generator zależności dla plików C/C++
Name:		fastdep
Version:	0.16
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	http://www.irule.be/bvh/c++/fastdep/%{name}-%{version}.tar.gz
# Source0-md5:	838c08b790a5dfe9a50a4aec7947bc54
URL:		http://www.irule.be/bvh/c++/fastdep/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fastdep is (will be) a fast dependency generator for C/C++ files.

%description -l pl.UTF-8
fastdep jest (będzie) szybkim generatorem zależności dla plików C/C++.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D fastdep $RPM_BUILD_ROOT%{_bindir}/fastdep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
